import torch


def predict_with_inserted_output_vqc(
    trained_qlstm_model,
    x_window,
    inserted_expvals,
    target_timestep,
):
    inserted_output_q = torch.tensor(
        inserted_expvals,
        dtype=torch.float32,
    ).unsqueeze(0)

    h_t = torch.zeros(1, trained_qlstm_model.hidden_size, dtype=torch.float32)
    c_t = torch.zeros(1, trained_qlstm_model.hidden_size, dtype=torch.float32)

    trained_qlstm_model.eval()
    seq_len = x_window.shape[1]

    with torch.no_grad():
        for timestep in range(seq_len):
            x_t = x_window[:, timestep, :]
            combined = torch.cat([h_t, x_t], dim=-1)
            quantum_inputs = trained_qlstm_model.encoder(combined).squeeze(0)

            forget_q = trained_qlstm_model.vqc_forget(quantum_inputs).unsqueeze(0)
            input_q = trained_qlstm_model.vqc_input(quantum_inputs).unsqueeze(0)
            candidate_q = trained_qlstm_model.vqc_candidate(quantum_inputs).unsqueeze(0)

            if timestep == target_timestep:
                output_q = inserted_output_q
            else:
                output_q = trained_qlstm_model.vqc_output(quantum_inputs).unsqueeze(0)

            forget_gate = torch.sigmoid(trained_qlstm_model.forget_decoder(forget_q))
            input_gate = torch.sigmoid(trained_qlstm_model.input_decoder(input_q))
            candidate_gate = torch.tanh(trained_qlstm_model.candidate_decoder(candidate_q))
            output_gate = torch.sigmoid(trained_qlstm_model.output_decoder(output_q))

            c_t = forget_gate * c_t + input_gate * candidate_gate
            h_t = output_gate * torch.tanh(c_t)

        prediction = trained_qlstm_model.output_head(h_t)

    return prediction.squeeze().item()

# Quantum Computing for Earth Observation

Tutorial at the [XXV ISPRS Congress](https://www.isprs2026toronto.com/), Toronto, Canada, 4 to 11 July 2026.

---

## Overview

The session combines presentation talks with hands-on notebooks on quantum computing for Earth observation and remote sensing time series analysis.

The quantum computing talks introduce the mathematical framework for quantum computing and how qubits and quantum operations are represented. Topics include quantum gates, measurement in quantum circuits, data encoding, and examples of quantum algorithms.

The remote sensing talks introduce the Normalized Difference Vegetation Index (NDVI), its importance in vegetation monitoring, and how the data for the case study were collected and prepared.

The hands-on component covers machine learning concepts for time series analysis and introductory quantum circuit tutorials in Python. Building on these concepts, the hands-on component applies a quantum machine learning workflow to forecast NDVI for the case study region.

---

## Session information


| Item           | Details                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------ |
| Congress       | [XXV ISPRS Congress](https://www.isprs2026toronto.com/onsite-information), Toronto, Canada |
| Congress dates | 4 to 11 July 2026                                                                          |
| Tutorial       | 4 July 2026, 8:30 a.m. to 5:00 p.m. Eastern Time |
| Venue          | [Metro Toronto Convention Centre](https://www.isprs2026toronto.com/onsite-information), Toronto, Ontario                                          |
| Room           | See the [full program](https://www.isprs2026toronto.com/full-program) for room details     |


---

## Tutorial schedule


| Time        | Topic                                           |
| ----------- | ----------------------------------------------- |
| 8:30–8:45   | Welcome and overview                            |
| 8:45–10:00  | Introduction to quantum computing               |
| 10:00–10:30 | Break                                           |
| 10:30–11:00 | Introduction to quantum computing (continued)   |
| 11:00–12:15 | Remote sensing, NDVI, and data collection       |
| 12:15–1:30  | Break                                           |
| 1:30–3:00   | LSTM fundamentals and quantum circuit tutorials |
| 3:00–3:30   | Break                                           |
| 3:30–4:45   | QLSTM case study and circuit execution          |
| 4:45–5:00   | Wrap-up                                         |


---

## Setup

The recommended way to follow the hands-on labs and live demo is to set up a Python 3.12 environment.

General dependencies include NumPy (>= 2.0), PyTorch, Matplotlib, Rasterio, and GeoPandas. Quantum computing dependencies include [PennyLane](https://pypi.org/project/Pennylane/), [Qiskit](https://pypi.org/project/qiskit/) (>= 2.0), and [Qiskit IBM Runtime](https://pypi.org/project/qiskit-ibm-runtime/).

[Google Colab](https://colab.research.google.com/) is the recommended way to follow along during the live tutorial. A [Google account](https://accounts.google.com/) is required.

To clone the repository locally with Git installed, run the following commands:

```bash
git clone https://github.com/MahkameSalimi/ISPRS-Tutorial.git
cd ISPRS-Tutorial
```

For a local environment, use [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) or [Miniforge](https://github.com/conda-forge/miniforge) with the `env.yml` file at the repository root. This installs Python 3.12, PyTorch, the geospatial stack, and the quantum packages needed for the tutorial.

From the repository root:

```bash
conda env create -f env.yml
conda activate qcfeo-isprs
jupyter notebook
```

To verify the installation, run the following from the command line with the environment activated:


```bash
python -c "import torch, pennylane, qiskit, qiskit_aer, rasterio, geopandas; print('OK')"
```

---

## IBM Quantum access

During the live tutorial, we will walk through submitting jobs to IBM Quantum hardware.

Registered participants are expected to have received access through a [PINQ²](https://www.pinq2.com/en/) account on the [IBM Quantum Platform](https://quantum.cloud.ibm.com/).

Participants can also create a free IBM Quantum Platform account, which currently includes 10 minutes of execution time per month on IBM quantum processing units. See the [IBM Quantum Platform](https://quantum.cloud.ibm.com/) for current account details and registration information.

Additional instructions for job submission will be provided during the hands-on session. Live hardware execution depends on queue time and backend availability. 

Where possible, setting up access to the quantum platform before the tutorial is recommended.

---

## Contact

Tutorial instructors and organizers:


| Name                    | Contact                                                                                     | Affiliation                                             |
| ----------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Dr. Shahpoor Moradi     | [moradis@ucalgary.ca](mailto:moradis@ucalgary.ca)                                           | University of Calgary                                   |
| Dr. Stefania Amici      | [stefania.amici@ingv.it](mailto:stefania.amici@ingv.it)                                     | National Institute of Geophysics and Volcanology (INGV) |
| Dr. Vittorio Cannas     | [vittorio.cannas@ingv.it](mailto:vittorio.cannas@ingv.it)                                   | INGV                                                    |
| Dr. Mozhdeh Shahbazi    | [mozhdeh.shahbazi@nrcan-rncan.gc.ca](mailto:mozhdeh.shahbazi@nrcan-rncan.gc.ca)             | Natural Resources Canada (NRCan)                        |
| Mahkame Salimi Moghadam | [mahkame.salimimoghadam@nrcan-rncan.gc.ca](mailto:mahkame.salimimoghadam@nrcan-rncan.gc.ca) | University of Calgary / NRCan                           |
| Sohrab Ganjian          | [sohrab.ganjian@nrcan-rncan.gc.ca](mailto:sohrab.ganjian@nrcan-rncan.gc.ca)                 | NRCan                                                   |



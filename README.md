# Mock Bank FS Hackathon

This repository contains a full‑stack mock banking application created for a hackathon. The project runs **three servers** that work together to simulate a simple banking system.

---

## Prerequisites

Make sure you have the following installed on your machine:

* **Python 3.13**

---

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/jeffersonCueva/mock-bank-fs-hackathon.git
   cd mock-bank-fs-hackathon
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
2. **Add Environment Variables**

   ```json
   COSMOS_ENDPOINT= "<insert endpoint here>"
   COSMOS_KEY= "<insert key here>"
   COSMOS_DATABASE="mock-bank-db"

   ```

---

## Running the Project

This project uses a batch script to start **all three servers at once**.

1. From the root directory of the project, run:

   ```bash
   run_all.bat
   ```

2. The script will automatically:

   * Start all backend services
   * Open separate terminals for each server (if configured)

3. Wait until all servers show they are running before interacting with the application.


---

## Notes

* This project is intended for **development and demo purposes only**.
* If a port is already in use, stop the conflicting service or update the configuration.
* If you encounter permission issues, try running the terminal as **Administrator**.

---

## Troubleshooting

* **Dependencies not installing?**

  * Ensure you're using the correct Python version:

    ```bash
    python --version
    ```

* **Servers not starting?**

  * Check the terminal output for errors.
  * Verify all required environment variables (if any) are set.

---

## License

This project was created for a hackathon and is provided as‑is.


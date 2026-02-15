# **bonus: (decouple compute and storage)**
## `track the data versions using google drive as storage`

## Problem Statement

The bonus task required implementing:

> **Decoupling compute and storage** by configuring Google Drive as a DVC remote backend.

Instead of storing dataset versions only on the local machine, the objective was to:

* Track dataset versions using DVC
* Store actual data versions in Google Drive
* Keep local machine responsible only for computation
* Demonstrate reproducibility using remote-backed storage

This simulates a real-world MLOps architecture where compute and storage are separated.


## Solution Approach

### 🔹 Step 1 – Local Data Versioning

* Initialized Git and DVC repository
* Generated dataset splits using seeds: [ 2, 9, 13, 42, 123 ]
* Tracked dataset versions using:

  ```bash
  dvc add data/
  git commit
  ```


### 🔹 Step 2 – Configure Google Drive as Remote Storage

Configured Google Drive as DVC remote backend:

```bash
dvc remote add -d myremote gdrive://<folder_id>
```

Then configured OAuth authentication:

* Enabled Google Drive API
* Configured OAuth consent screen
* Set app type to **External**
* Added personal Gmail as **Test User**
* Created OAuth Client ID (Desktop App)
* Configured DVC with:

  ```bash
  dvc remote modify myremote gdrive_client_id <client_id>
  dvc remote modify myremote gdrive_client_secret <client_secret>
  ```

---

### 🔹 Step 3 – Push Data to Google Drive

Executed:

```bash
dvc push
```

Result:

```
Authentication successful.
6 files pushed
```

Google Drive now stores DVC cache objects (MD5 hashed structure).


### Git Log (Bonus Implementation)

```
fd78ce1 Data split seed=123
d2fa0d6 Data split seed=42
9d31918 Data split seed=13
f15df85 Data split seed=9
5743e7c Data split seed=2
fbd9dfd Configured Google Drive as DVC remote storage (bonus)
ce48807 Track data in copied project
1f4a0d6 Configured Google Drive as DVC remote
d61cb28 Initialize DVC
```

This shows:

* Initial DVC setup
* Google Drive remote configuration
* Multiple dataset versions pushed remotely


## Architecture After Decoupling

### 💻 Local Machine (Compute Layer)

* `prepare.ipynb`
* `train.ipynb`
* Git metadata
* DVC metadata (`.dvc` files)
* MLflow experiment tracking

### ☁ Google Drive (Storage Layer)

* DVC content-addressable cache
* All dataset versions
* Backup of historical data splits


## Verification of Decoupling

To validate separation:

1. Deleted local `data/` folder

2. Executed:

   ```bash
   dvc pull
   ```

3. Data restored from Google Drive successfully

This proves:

```
Local machine ≠ Source of truth
Google Drive = Authoritative data storage
```



## Industrial Relevance

This mirrors real-world MLOps systems:

| Local Compute       | Remote Storage           |
| ------------------- | ------------------------ |
| Training models     | S3 / GCS / Azure Blob    |
| Feature engineering | Versioned object storage |
| Experimentation     | Centralized data lake    |

Using Google Drive as remote simulates:

* Cloud storage backend
* Scalable data management
* Reproducible ML pipelines
* Machine-independent workflows


## Result

* Successfully decoupled compute and storage
* Data versions stored remotely via DVC
* Git tracks metadata only
* Google Drive stores actual dataset objects
* Fully reproducible pipeline across machines


## 🚀 Final System Design

```
Git         → Metadata version control
DVC         → Data version tracking
Google Drive→ Remote storage backend
MLflow      → Experiment & model tracking
```

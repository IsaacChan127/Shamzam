# Shamzam — Shazam-Like Audio Recognition (Microservices MVP)

## Overview

**Shamzam** is a Shazam-like system built using Python microservices and REST APIs.
It allows administrators to manage a music catalogue and enables users to identify songs from short audio fragments.

---

## How It Works

### Administrator Features

**Add Track (S1)**
Adds a music track to the catalogue database.

**Remove Track (S2)**
Deletes a music track so it is no longer available.

**List Tracks (S3)**
Displays all tracks currently stored in the catalogue.

---

### User Feature

**Identify Song From Audio (S4)**
A user uploads an audio fragment. The system sends the audio to the **Audd.io API** for recognition and matches the result with tracks stored in the catalogue.

---

## System Components

* **Catalogue Service**

  * Stores tracks in an SQLite database.
  * Handles add, remove, and list operations.

* **Recognition Service**

  * Accepts audio fragments.
  * Uses Audd.io to recognise songs.

Each service exposes REST API endpoints using JSON input and output.

---

## Technology Stack

* Python
* REST APIs
* SQLite Database
* Audd.io Audio Recognition API

---

## Running the System

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Start the microservices.

3. Use REST requests to:

* add or remove tracks,
* list catalogue contents,
* recognise songs from audio fragments.

---

## Testing

End-to-end tests cover:

* Successful requests (happy paths)
* Invalid inputs
* Processing or communication failures.

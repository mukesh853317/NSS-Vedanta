# NSS Digital Management System - Version 1

A local-first NSS activity and documentation management application built with Streamlit and SQLite.

## Included in Version 1

- Dashboard
- Academic year / college settings
- NSS activity management
- Volunteer management
- Attendance
- Activity document/evidence upload
- SQLite database
- Searchable activity and volunteer records

## Run

1. Install Python 3.10+.
2. Open a terminal in this project folder.
3. Create a virtual environment (recommended).
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Start the application:

```bash
streamlit run app.py
```

6. Open the local URL shown by Streamlit, usually:

http://localhost:8501

## Data

The database is stored in `data/nss.db`.

Uploaded activity documents are stored in `documents/<activity-code>/`.

## Important

Version 1 is intentionally local-first. Before institutional/cloud deployment, add authentication, role permissions, automated backups, audit logs, cloud file storage, and secure document access.

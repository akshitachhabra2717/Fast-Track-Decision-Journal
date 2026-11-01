# Fast-Track-Decision-Journal
# Decision Journal

A simple app to score and track important decisions using weighted criteria (cost, risk, growth).

**Live App:** https://fast-track-decision-journal-n2zajntwpketltrdsrjxte.streamlit.app/

## DevOps Pipeline

| Stage | Tool |
|---|---|
| Version Control | GitHub |
| CI | GitHub Actions (lint + compile check) |
| CD | Streamlit Community Cloud (auto-deploy on push) |
| Monitoring | Grafana Cloud Synthetic Monitoring (uptime + latency) |

## Monitoring

<img width="700" alt="Grafana monitoring" src="https://github.com/user-attachments/assets/f7d5de45-635b-4052-b950-dfea4d93b01e" />

*Note: Free Streamlit apps sleep after inactivity, so the first request can be slow.*

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```


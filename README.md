# 🏥 Medi-Locator — Hyperlocal Medicine Availability Portal

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://python.org)
[![Django](https://img.shields.io/badge/Django-Framework-green?style=flat-square&logo=django)](https://djangoproject.com)
[![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite)](https://sqlite.org)
[![Status](https://img.shields.io/badge/Status-Live%20MVP-brightgreen?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)]()

> **Finding a medicine shouldn't feel like an emergency of its own.**  
> Medi-Locator connects medicine seekers with nearby pharmacies — through map-based search, real-time store visibility, and a broadcast request system — so the right medicine reaches the right person, fast.

---

## 🔍 The Problem

When someone needs a specific medicine urgently:
- They visit store after store with no guarantee of availability
- There's no centralized platform to check stock across pharmacies
- Delays are dangerous — especially at odd hours, in emergencies, or for rare medicines

**Medi-Locator solves this.** One search. All nearby pharmacies. Instant contact.

---

## ✨ Features

### For Users (Medicine Seekers)
| Feature | Description |
|---|---|
| 🗺️ Map-Based Search | Find pharmacies near a location on an interactive map |
| 💊 Medicine Request | Broadcast a request to all registered pharmacies at once |
| 📬 Request Tracking | Update request status once medicine is received |
| ⭐ Feedback System | Rate and review stores after visiting |
| 📞 Contact Admin | Raise issues or queries through a built-in contact form |

### For Shop Owners (Pharmacies)
| Feature | Description |
|---|---|
| 🏪 Shop Dashboard | Manage store profile, address, and contact details |
| 📍 Map Registration | Pin exact shop location so users can find you geographically |
| 📥 Receive Requests | View medicine requests broadcast by nearby users |
| 📲 Direct Contact | Reach users directly via WhatsApp when you have their medicine |

---

## 🛠️ Tech Stack

```
Backend     → Python 3.x · Django
Database    → SQLite
Frontend    → HTML · CSS · JavaScript
Maps        → Interactive Map Integration (Geolocation-based)
IDE         → Visual Studio Code
OS          → Windows
```

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Medi-Locator                      │
├──────────────────┬──────────────────────────────────┤
│   USER PORTAL    │        SHOP OWNER PORTAL          │
│                  │                                   │
│  Register/Login  │       Register/Login              │
│  Search on Map   │       Add Shop + Pin Location     │
│  Send Request    │       View Incoming Requests      │
│  Track Status    │       Contact Users (WhatsApp)    │
│  Give Feedback   │       Manage Profile              │
└──────────────────┴──────────────────────────────────┘
                        │
               ┌────────▼────────┐
               │   Django ORM    │
               │   SQLite DB     │
               └─────────────────┘
```

---

## 📦 Modules

1. **Registration Management** — Separate sign-up flows for users and shop owners
2. **Login Management** — Secure email + password authentication
3. **Profile Management** — Update name, address, and contact info
4. **Shop & Map Integration** — Owners pin their shop location; users discover stores geographically
5. **Search & Filter** — Location-based pharmacy discovery on an interactive map
6. **Medicine Request System** — Broadcast requests to all pharmacies; owners respond directly
7. **Contact Management** — Users report issues to admin
8. **Feedback Management** — Post-visit reviews and platform ratings

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.x
pip
Git
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/sanskritika2409/medi-locator.git
cd medi-locator

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser (admin)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000`

---

## 📁 Project Structure

```
medi-locator/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── medilocator/              # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/                    # User registration, login, profile
├── shops/                    # Shop owner dashboard, map integration
├── requests/                 # Medicine request & broadcast system
├── feedback/                 # Feedback and contact modules
│
└── templates/                # HTML templates
    ├── base.html
    ├── user/
    └── shop/
```

---

## 🔮 Future Scope

- [ ] In-app messaging between users and pharmacies
- [ ] Medicine inventory management for shop owners
- [ ] Home delivery integration
- [ ] Prescription upload feature
- [ ] Expand to hospitals, diagnostic labs, and ambulance services
- [ ] Mobile app (Android/iOS)

---

## ⚠️ Known Limitations

- Location accuracy may vary in remote areas
- Requires a stable internet connection
- Currently web-only (no mobile app)

---

## 👩‍💻 Author

**Sanskritika Awasthi**  
BTech Computer Science · Data Science & AI (IBM Collaborative Program)  
Shri Ramswaroop Memorial University, Lucknow

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/sanskritika-awasthi-9400592a6)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=flat-square&logo=github)](https://github.com/sanskritika2409)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat-square&logo=gmail)](mailto:awasthisanskritika@gmail.com)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> *Built during internship at Precursor Info Solutions (June – August 2025) — shipped from zero to live MVP in 10 weeks.*

# 🚀 GitHub User Activity CLI

A simple and clean command-line interface (CLI) tool that fetches and displays the recent GitHub activity of any user directly in your terminal.

This project helps practice:

* Working with APIs
* Handling JSON data
* CLI development in Python
* Clean terminal output using **rich**

---

## 📦 Installation & Setup

Create virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

---

## ▶️ Usage

Run the CLI tool from terminal:

```bash
python3 events.py <github_username>
```

Example:

```bash
python3 events.py torvalds
```

---

## 🖥️ Example Output

```
Latest events for torvalds

🚀 pushed 3 commits to linux
⭐ starred repo-name
🔀 opened pull request #21
🐛 closed issue #5
🌱 created branch dev
```

---

## 🛠️ Technologies Used

* Python
* Requests
* Rich (for colored terminal output)
* GitHub REST API

---

## 🌐 GitHub API Endpoint

```
https://api.github.com/users/<username>/events
```

---

## 📌 Notes

* Internet connection required
* GitHub rate limits may apply if too many requests are made
* Only public events are displayed

---

## 👨‍💻 Author

Built as a backend practice project for working with APIs and building CLI tools in Python.

https://roadmap.sh/projects/github-user-activity project link

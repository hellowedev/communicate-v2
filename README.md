# Communicate v2.1.0

A lightweight, open‑source “Share” app, that lets users publish posts with title, description, and an image. You can share your thoughts and ideas, and everyone can see them—even people who aren't logged in.

---

## 🚀 Features

* Create a Share
– Logged-in users can create a Share with a title, description, and optional image.

* View All Shares
– Everyone (even without logging in) can view all Shares.

* Edit & Delete
– Only the creator of a Share can edit or delete it.

* Built with Django & Tailwind CSS
– Django powers the backend logic, while Tailwind CSS enables fast, utility-first styling for rapid UI development.
---

## 📦 Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/hellowedev/communi-v2.git
   cd communicate-v2
   ```

2. **Create a virtual environment & install dependencies**

   ```bash
   python3 -m venv .venv
   source ./.venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure your environment**
   Copy the example and fill in your secrets:

   ```bash
   cp .env.example .env
   # then edit .env
   ```

4. **Setup tailwindcss (only run for first time to setup input css file for tailwind css)**

   ```bash
   npm install
   ./tailwind-installer.sh ./css/global.css
   ```

5. **Initialize the database & collect static files**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**

   ```bash
   # In 1 terminal run the python django development server 
   python manage.py runserver
   ```

   ```bash
   # In a separate terminal, start the Tailwind CSS watcher to compile styles
   npm run tailwind:watch
   ```

---

## 📌 Roadmap & Todo

1. **Fix image uploads**

   * Ensure image uploads work in deployements
   * Add server‑side validation for file size anf file type
2. **💬 Comments & Reactions**

   * Let users like or bookmark Shares.
3. **🚀 Pagination & Filtering**
   * Infinite scroll or “Load more” button.
   * Filter by date, title, description and tags.
4. **🌐 OAuth Login**

   * Enable authentication with Google, GitHub, Twitter OAuth.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/xyz`)
3. Commit your changes (`git commit -m "Add xyz"`)
4. Push (`git push origin feature/xyz`) and open a Pull Request

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

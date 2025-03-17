import os

project_name = "laravel-test"
repo_url = "https://github.com/alexm-cell/projetlaravelmesseinalexandre.git"

commands = [
    f"composer create-project laravel/laravel {project_name}",
    f"cd {project_name} && cp .env.example .env",
    "php artisan key:generate",
    "composer require laravel/breeze --dev",
    "php artisan breeze:install blade",
    "npm install",
    "npm run dev",
    "php artisan migrate",
    "composer require livewire/livewire",
    "php artisan make:livewire BookingManager",
    "composer require filament/filament",
    "php artisan make:filament-user",
    "git init",
    f"git remote add origin {repo_url}",
    "git add .",
    "git commit -m 'Initialisation du projet Laravel'",
    "git branch -M main",
    "git push -u origin main"
]

for cmd in commands:
    os.system(cmd)

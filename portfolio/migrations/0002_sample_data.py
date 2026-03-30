from django.db import migrations


def add_sample_data(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    Education = apps.get_model('portfolio', 'Education')

    # Profile
    Profile.objects.create(
        name="Your Full Name",
        tagline="Full-Stack Developer & Problem Solver",
        bio="Hi! I'm a passionate developer who loves building clean, efficient, and user-friendly web applications. I enjoy turning complex problems into simple, beautiful solutions.\n\nWith experience in Python, Django, and modern web technologies, I strive to write code that is not only functional but also maintainable and scalable.",
        career_interests="I'm deeply interested in backend web development, cloud deployment, and building applications that make a real difference. My goal is to work on impactful projects with collaborative teams, and to keep growing as a full-stack developer.",
        email="yourname@email.com",
        github="https://github.com/yourusername",
        linkedin="https://linkedin.com/in/yourusername",
    )

    # Skills
    skills_data = [
        ('Python', 'language', 1),
        ('JavaScript', 'language', 2),
        ('HTML5', 'language', 3),
        ('CSS3', 'language', 4),
        ('SQL', 'language', 5),
        ('Django', 'framework', 1),
        ('Bootstrap', 'framework', 2),
        ('jQuery', 'framework', 3),
        ('Git & GitHub', 'tool', 1),
        ('PyCharm', 'tool', 2),
        ('MySQL', 'tool', 3),
        ('PythonAnywhere', 'tool', 4),
        ('VS Code', 'tool', 5),
        ('REST APIs', 'other', 1),
        ('Django Admin', 'other', 2),
        ('Responsive Design', 'other', 3),
    ]
    for name, cat, order in skills_data:
        Skill.objects.create(name=name, category=cat, order=order)

    # Projects
    projects_data = [
        {
            'title': 'Personal Portfolio Website',
            'description': 'A dynamic portfolio website built with Django, featuring sections for personal info, projects, skills, and a contact form. Deployed on PythonAnywhere with MySQL database.',
            'technologies': 'Django, Python, HTML, CSS, JavaScript, MySQL',
            'github_link': 'https://github.com/yourusername/portfolio',
            'order': 1,
        },
        {
            'title': 'Task Management App',
            'description': 'A full-featured task management application with user authentication, task categories, due dates, and priority levels. Built using Django with a clean Bootstrap UI.',
            'technologies': 'Django, Python, Bootstrap, SQLite',
            'github_link': 'https://github.com/yourusername/task-app',
            'order': 2,
        },
        {
            'title': 'Weather Dashboard',
            'description': 'A weather dashboard that fetches real-time data from the OpenWeatherMap API, displays current conditions and 5-day forecasts with interactive charts.',
            'technologies': 'Python, Django, JavaScript, REST API',
            'github_link': 'https://github.com/yourusername/weather-app',
            'order': 3,
        },
    ]
    for p in projects_data:
        Project.objects.create(**p)

    # Education
    Education.objects.create(
        school="Your University Name",
        degree="Bachelor of Science",
        program="Information Technology",
        year_start=2022,
        year_end=None,
        description="Currently pursuing a degree focused on software development, databases, networking, and systems analysis.",
    )


def remove_sample_data(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    Education = apps.get_model('portfolio', 'Education')
    Profile.objects.all().delete()
    Skill.objects.all().delete()
    Project.objects.all().delete()
    Education.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(add_sample_data, remove_sample_data),
    ]

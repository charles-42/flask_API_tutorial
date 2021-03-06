"""
A partir du dictionnaire suivant creer une API qui permet:
- d'obtenir la liste des chaines youtubes
- d'obtenir les informations d'une chaine
- de créer une nouvelle chaine, assurez vous que les informations envoyées soient exactes
- de supprimer une chaine
- de modifier la langue d'une chaine
- d'obtenir toutes les chaines d'une langue
- d'ajouter un sujet à une chaine
- d'obtenir toutes les chaines sur un certain sujet

Pour aller plus loin:
- testez votre application (avec des tests automatiques en pytest)
- protéger votre route "delete channel" grâce à un système d'authentification.  
"""

channel_dictionary = {
    "Tech_With_Time": {
        "title": "Tech_With_Time",
        "description": "Learn programming, software engineering, machine learning and everything tech from this channel. With a special emphasis on python and javascript my channel aims to give you free resources so that you can learn to code and dive into the software engineering and programming industry. My goal is to provide the highest quality programming and tech videos on the internet! ",
        "url": "https://www.youtube.com/c/TechWithTim/about",
        "language": "English",
        "subjects": ["Flask","Python"],
        "image_url":"https://yt3.ggpht.com/ytc/AKedOLQXx-JXf1NsSUtVHcYhx4B4MaIYE0m7I_H0GHmu-w=s900-c-k-c0x00ffffff-no-rj"
        },
    "Docstring": {
        "title": "Docstring",
        "description": "Tutoriels, trucs & astuces, bonnes pratiques autour du langage Python, de différents framework (Django, Qt for Python...) et du développement en général.",
        "url": "https://www.youtube.com/c/Docstring/featured",
        "language": "French",
        "subjects": ["Python"],
        "image_url":"https://yt3.ggpht.com/3sXh0-ipDGiHgBRTle8sbGLjKm6p0PENZAeoo2-H_w3NxOLXLI7Khw2ZEi7olJNs2kMNEcql=s900-c-k-c0x00ffffff-no-rj"
        },

    "ArjanCodes": {
        "title": "ArjanCodes",
        "description": "On this channel, I post videos about programming and software design to help you take your coding skills to the next level. I'm an entrepreneur and a university lecturer in computer science, with more than 20 years of experience in software development and design. If you're a software developer and you want to improve your development skills, and learn more about programming in general, make sure to subscribe for helpful videos.",
        "url": "https://www.youtube.com/c/ArjanCodes/featured",
        "language": "English",
        "subjects": ["Python","POO"],
        "image_url":"https://yt3.ggpht.com/PF_5a9pF_CurRWcBpGxAvYv-uMc6bsK_LYpmgHDMDnG5tTzHbYU7Jz55pU_QXm1f0nVLTmlzZw=s900-c-k-c0x00ffffff-no-rj"
        }
    }
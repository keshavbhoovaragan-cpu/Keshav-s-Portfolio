import os

pages = {
    'index.html': ('Keshav Bhoovaragan — SDE Intern @ IBM | ML Engineer | Portfolio', 'Business + ML + SWE hybrid. SDE Intern at IBM, ML Engineer at Ascendion. UMD Smith School 27. Building AI systems at the intersection of machine learning, backend engineering, and business analytics.', 'https://keshavbhoovaragan-cpu.github.io/Keshav-s-Portfolio/'),
    'about.html': ('About — Keshav Bhoovaragan', 'Why hire Keshav? Business + ML + SWE hybrid with real enterprise AI experience at IBM and Ascendion. OMBA and Information Risk Management at UMD Smith School.', 'https://keshavbhoovaragan-cpu.github.io/Keshav-s-Portfolio/about.html'),
    'experience.html': ('Experience — Keshav Bhoovaragan', 'SDE Intern at IBM San Jose. ML Engineer Intern at Ascendion. B.S. Operations Management and Business Analytics plus Information Risk Management at UMD Smith School.', 'https://keshavbhoovaragan-cpu.github.io/Keshav-s-Portfolio/experience.html'),
    'projects.html': ('Projects — Keshav Bhoovaragan', 'Healthcare AI chatbot, Criminal Justice recidivism ML (1st Place Inspirit AI), Meal Match food redistribution app. Built with Python, Flask, React, and more.', 'https://keshavbhoovaragan-cpu.github.io/Keshav-s-Portfolio/projects.html'),
    'skills.html': ('Skills — Keshav Bhoovaragan', '35+ skills across ML, Python, Flask, React, SQL, Azure, NLP, AI Ethics, Business Analytics, and more.', 'https://keshavbhoovaragan-cpu.github.io/Keshav-s-Portfolio/skills.html'),
    'contact.html': ('Contact — Keshav Bhoovaragan', 'Get in touch with Keshav Bhoovaragan. Open to full-time SWE/SDE roles and co-ops for 2027.', 'https://keshavbhoovaragan-cpu.github.io/Keshav-s-Portfolio/contact.html'),
}

og_image = 'https://keshavbhoovaragan-cpu.github.io/Keshav-s-Portfolio/og-image.png'

for fname, (title, desc, url) in pages.items():
    path = os.path.expanduser('~/portfolio/' + fname)
    with open(path) as f:
        c = f.read()
    meta = '<meta name="description" content="' + desc + '">\n<meta name="author" content="Keshav Bhoovaragan">\n<meta property="og:title" content="' + title + '">\n<meta property="og:description" content="' + desc + '">\n<meta property="og:image" content="' + og_image + '">\n<meta property="og:url" content="' + url + '">\n<meta property="og:type" content="website">\n<meta name="twitter:card" content="summary_large_image">\n<meta name="twitter:title" content="' + title + '">\n<meta name="twitter:description" content="' + desc + '">\n<meta name="twitter:image" content="' + og_image + '">'
    c = c.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + meta)
    old_title = c[c.find('<title>'):c.find('</title>')+8]
    c = c.replace(old_title, '<title>' + title + '</title>')
    with open(path, 'w') as f:
        f.write(c)
    print('done: ' + fname)

print('all done')

import os

files = {}
for f in ['index.html','experience.html','projects.html','skills.html','contact.html']:
    with open(os.path.expanduser('~/portfolio/'+f)) as fh:
        files[f] = fh.read()

exp = files['experience.html']
nav = exp[exp.find('<nav'):exp.find('</nav>')+6]
footer = exp[exp.find('<footer>'):exp.find('</footer>')+9]

about = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>About — Keshav Bhoovaragan</title>\n<link rel="stylesheet" href="style.css">\n<style>\n  .about-hero{padding:72px 40px 40px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:flex-end;position:relative;overflow:hidden;}\n  .page-hero-bg{font-family:"Bebas Neue",sans-serif;font-size:clamp(100px,18vw,220px);color:var(--cream2);line-height:1;letter-spacing:4px;position:absolute;right:-20px;bottom:-20px;pointer-events:none;user-select:none;z-index:0;}\n  .about-hero>*{position:relative;z-index:1;}\n  .sec-tag{font-family:"IBM Plex Mono",monospace;font-size:10px;color:var(--orange);letter-spacing:3px;text-transform:uppercase;margin-bottom:16px;display:flex;align-items:center;gap:10px;}\n  .sec-tag::before{content:"";display:inline-block;width:24px;height:1px;background:var(--orange);}\n  .sec-title{font-family:"Bebas Neue",sans-serif;font-size:clamp(48px,8vw,96px);letter-spacing:2px;line-height:1;color:var(--ink);margin:0;}\n  .about-section{border-top:1px solid var(--border);padding:48px 40px;}\n  .section-label{font-family:"IBM Plex Mono",monospace;font-size:10px;color:var(--orange);letter-spacing:2px;margin-bottom:32px;}\n  @media(max-width:768px){.about-hero{padding:48px 20px 32px;}.about-section{padding:32px 20px;}.three-col{grid-template-columns:1fr!important;}}\n</style>\n</head>\n<body>\n'
about += nav
about += '\n<div class="page-wrap page-enter">\n  <div class="about-hero">\n    <div>\n      <div class="sec-tag">About Me</div>\n      <h1 class="sec-title">WHO I AM<br>&amp; WHY IT MATTERS</h1>\n    </div>\n    <div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--muted);letter-spacing:1px;line-height:2;text-align:right;">\n      <div>Business + ML + SWE</div>\n      <div>IBM SDE Intern 2026</div>\n      <div>UMD Smith School \'27</div>\n    </div>\n    <div class="page-hero-bg">KB</div>\n  </div>\n\n  <div class="about-section">\n    <div class="section-label">// WHY HIRE ME</div>\n    <div class="three-col" style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px;">\n      <div style="border:1px solid var(--border);padding:28px 24px;"><div style="font-family:\'Bebas Neue\',sans-serif;font-size:22px;letter-spacing:1px;margin-bottom:10px;">Business + Tech</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;color:var(--muted);line-height:1.8;">Most engineers cannot talk business. Most business majors cannot code. I do both — OMBA + Information Risk Management + 2 ML internships + IBM SDE.</div></div>\n      <div style="border:1px solid var(--border);padding:28px 24px;"><div style="font-family:\'Bebas Neue\',sans-serif;font-size:22px;letter-spacing:1px;margin-bottom:10px;">Real Enterprise AI</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;color:var(--muted);line-height:1.8;">Not just academic projects. Built production Flask APIs, watsonx AI systems, and clinical trial ML pipelines at enterprise scale across 50+ sites.</div></div>\n      <div style="border:1px solid var(--border);padding:28px 24px;"><div style="font-family:\'Bebas Neue\',sans-serif;font-size:22px;letter-spacing:1px;margin-bottom:10px;">Proven Results</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;color:var(--muted);line-height:1.8;">~20% diagnostic accuracy boost. ~30% latency reduction. 1st Place AI algorithm at Inspirit AI Stanford. Presidential Scholarship recipient.</div></div>\n    </div>\n  </div>\n\n  <div class="about-section">\n    <div class="section-label">// GITHUB ACTIVITY</div>\n    <img src="https://ghchart.rshah.org/e8530a/keshavbhoovaragan-cpu" alt="GitHub contributions" style="width:100%;border:1px solid var(--border);padding:16px;box-sizing:border-box;"/>\n  </div>\n\n  <div class="about-section">\n    <div class="section-label">// CURRENTLY LEARNING</div>\n    <div style="display:flex;flex-wrap:wrap;gap:12px;">\n      <span style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;border:1px solid var(--border);padding:6px 14px;">Agentic AI Systems</span>\n      <span style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;border:1px solid var(--border);padding:6px 14px;">watsonx Platform</span>\n      <span style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;border:1px solid var(--border);padding:6px 14px;">LLM Fine-tuning</span>\n      <span style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;border:1px solid var(--border);padding:6px 14px;">Cloud-Native Backend</span>\n      <span style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;border:1px solid var(--border);padding:6px 14px;">TypeScript</span>\n      <span style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;border:1px solid var(--border);padding:6px 14px;">System Design</span>\n      <span style="font-family:\'IBM Plex Mono\',monospace;font-size:11px;border:1px solid var(--border);padding:6px 14px;">Docker &amp; Kubernetes</span>\n    </div>\n  </div>\n\n  <div class="about-section">\n    <div class="section-label">// BEYOND THE CODE</div>\n    <div style="display:flex;flex-wrap:wrap;gap:16px;">\n      <div style="border:1px solid var(--border);padding:16px 20px;display:flex;align-items:center;gap:10px;"><span style="font-size:20px;">🎾</span><div><div style="font-family:\'Bebas Neue\',sans-serif;font-size:16px;letter-spacing:1px;">Tennis</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--muted);">State Champ · CB South + UMD Club</div></div></div>\n      <div style="border:1px solid var(--border);padding:16px 20px;display:flex;align-items:center;gap:10px;"><span style="font-size:20px;">🎥</span><div><div style="font-family:\'Bebas Neue\',sans-serif;font-size:16px;letter-spacing:1px;">YouTube Creator</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--muted);">Tech with Keshav · @kbthetechboss9169</div></div></div>\n      <div style="border:1px solid var(--border);padding:16px 20px;display:flex;align-items:center;gap:10px;"><span style="font-size:20px;">💪</span><div><div style="font-family:\'Bebas Neue\',sans-serif;font-size:16px;letter-spacing:1px;">Gym</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--muted);">Daily discipline · strength training</div></div></div>\n      <div style="border:1px solid var(--border);padding:16px 20px;display:flex;align-items:center;gap:10px;"><span style="font-size:20px;">🏈</span><div><div style="font-family:\'Bebas Neue\',sans-serif;font-size:16px;letter-spacing:1px;">Football &amp; Basketball</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--muted);">Watching + playing casually</div></div></div>\n      <div style="border:1px solid var(--border);padding:16px 20px;display:flex;align-items:center;gap:10px;"><span style="font-size:20px;">🎵</span><div><div style="font-family:\'Bebas Neue\',sans-serif;font-size:16px;letter-spacing:1px;">Music</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--muted);">Always on while coding</div></div></div>\n      <div style="border:1px solid var(--border);padding:16px 20px;display:flex;align-items:center;gap:10px;"><span style="font-size:20px;">📺</span><div><div style="font-family:\'Bebas Neue\',sans-serif;font-size:16px;letter-spacing:1px;">Binging TV Shows</div><div style="font-family:\'IBM Plex Mono\',monospace;font-size:10px;color:var(--muted);">Certified binge-watcher</div></div></div>\n    </div>\n  </div>\n\n</div>\n'
about += footer
about += '\n<script src="shared.js"></script>\n</body>\n</html>'

with open(os.path.expanduser('~/portfolio/about.html'), 'w') as f:
    f.write(about)
print('about.html created')

# Clean index.html
idx = files['index.html']
cut_start = idx.find('\n<div style="border-top:1px solid var(--border);padding:48px 40px;">')
if cut_start == -1:
    cut_start = idx.find('\n<footer>')
cut_end = idx.find('\n<footer>')
idx = idx[:cut_start] + '\n\n' + idx[cut_end:]

idx = idx.replace(
    '<a href="contact.html" class="ql-card">\n        <div class="ql-num">04</div>\n        <div class="ql-title">Contact</div>\n        <div class="ql-sub">Full-time &amp; co-ops 2027<br>Reply within 24h</div>',
    '<a href="about.html" class="ql-card">\n        <div class="ql-num">04</div>\n        <div class="ql-title">About</div>\n        <div class="ql-sub">Why hire me · Interests<br>GitHub activity</div>'
)
idx = idx.replace(
    'HOME</a>\n    <a href="experience.html">EXPERIENCE',
    'HOME</a>\n    <a href="about.html">ABOUT</a>\n    <a href="experience.html">EXPERIENCE'
)
with open(os.path.expanduser('~/portfolio/index.html'), 'w') as f:
    f.write(idx)
print('index.html cleaned')

for fname in ['experience.html','projects.html','skills.html','contact.html']:
    c = files[fname]
    if '<li><a href="about.html">' not in c:
        c = c.replace('<li><a href="experience.html"', '<li><a href="about.html">About</a></li>\n      <li><a href="experience.html"')
    c = c.replace('<a href="index.html">HOME</a><a href="experience.html">', '<a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="experience.html">')
    with open(os.path.expanduser('~/portfolio/'+fname), 'w') as f:
        f.write(c)
    print('updated: ' + fname)

print('all done')

import json,re,html
from pathlib import Path
from datetime import date
base="https://samuel2samwell-dot.github.io/How-to-hire-a-hackers-"
cats={
"Cybersecurity":["security baseline","incident response","account protection","risk assessment","security awareness","backup planning","access control","vulnerability management","secure configuration","threat modeling"],
"Crypto Investigations":["exchange records","transaction timeline","wallet attribution","scam evidence","blockchain explorer","case documentation","cross-chain transfers","exchange compliance","fraud reporting","transaction tracing"],
"Private Investigation":["digital evidence","public-record research","case chronology","online identity checks","due diligence","evidence preservation","investigator selection","lawful research","report writing","privacy safeguards"],
"Asset Tracing":["asset inventory","public records","ownership verification","transaction records","beneficial ownership","evidence chain","cross-border records","risk indicators","professional referrals","recovery expectations"],
"Ethical Hacking":["written authorization","scope definition","web application testing","network assessment","responsible disclosure","remediation planning","test environment","access control review","security validation","report quality"],
"Blockchain Intelligence":["public ledger analysis","wallet clustering limits","token movement","transaction fees","bridge activity","on-chain indicators","address labeling","analytics limitations","evidence snapshots","privacy considerations"],
"Online Fraud Prevention":["phishing indicators","payment verification","impersonation scams","marketplace fraud","account recovery","evidence collection","reporting fraud","social engineering","safe communications","fraud prevention plan"],
"Digital Privacy":["privacy settings","data minimization","device security","metadata awareness","secure backups","identity exposure","account recovery","consent and monitoring","data access requests","privacy review"],
"Security News":["advisory review","patch prioritization","incident lessons","vulnerability disclosure","vendor notices","threat intelligence","security metrics","business continuity","supply-chain risk","security governance"],
"Offshore Legal Topics":["jurisdiction research","company records","beneficial ownership rules","cross-border compliance","document verification","professional advice","sanctions screening","tax-residency basics","legal process","record retention"]}
angles=["A practical checklist","A beginner guide","Common mistakes to avoid","Questions to ask a professional","How to document your findings","A risk-based approach","What records can and cannot show","Planning a responsible review","How to evaluate evidence","A step-by-step overview"]
def slug(s): return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")
def e(s): return html.escape(s,quote=True)
def page(title,cat,topic,slug,n,include_service_guidance=False):
 desc="Practical guidance on "+topic+", evidence quality, responsible research, legal scope and privacy."
 paras=[
 "Start by defining the question you need answered, the decision it supports, and the records you are lawfully entitled to access. A narrow written scope keeps research proportionate and makes conclusions easier to review. Identify the intended audience and the standard of evidence needed before collecting material.",
 "Prefer primary or otherwise reliable sources. Record source names, access dates, time zones, relevant identifiers and any limitations. Preserve original files where lawful, work from copies, and keep a log of what was collected and why. Screenshots can help but should not replace source records or context.",
 "Separate confirmed facts from assumptions and leads. A name match, wallet interaction, IP address, company filing or social profile may be incomplete or shared by unrelated people. Correlation alone does not prove identity, intent, ownership or misconduct. Record alternative explanations and seek independent corroboration.",
 "Use a repeatable workflow: define the question, identify permitted sources, collect the minimum necessary data, verify important details independently, document uncertainty, and set a stopping point. If personal information, financial activity or multiple jurisdictions are involved, check the applicable rules before proceeding.",
 "Common pitfalls include relying on screenshots without context, overlooking dates and currency units, trusting unsolicited recovery offers, or sharing more personal information than necessary. Never disclose passwords, private keys, seed phrases, one-time codes or remote-access credentials to an investigator or recovery service.",
 "Before choosing a provider, ask about experience, written scope, methodology, privacy and retention practices, pricing, conflicts of interest and report format. A responsible professional should explain what can realistically be established, what remains uncertain and which steps require a lawyer, regulator or other authorized organization."
 ]
 sections=["Understand the scope","Collect and preserve records","Interpret evidence carefully","Use a repeatable process","Avoid common risks","Choose qualified help"]
 body="".join("<h2>"+e(h)+"</h2><p>"+e(p)+"</p>" for h,p in zip(sections,paras))
 if include_service_guidance:
  service_notes = {
   "Hire a Hacker": "We can discuss authorized security testing for systems you own or have permission to test, including written scope, approved targets, safe test windows, prioritized findings and remediation guidance. Choose a provider that protects sensitive data and explains limitations; no assessment guarantees every weakness will be found.",
   "Private Investigator": "Lawful support may include open-source research, public-record checks, source verification, digital evidence organization and case chronologies. We help separate sourced facts from leads and document uncertainty so clients and qualified advisers can assess next steps. Findings are not guaranteed.",
   "News": "This series explains responsible cybersecurity, online fraud awareness, digital evidence and investigation practices. It aims to help readers understand common risks and practical next steps without sensational claims. Active security testing always requires explicit authorization.",
   "Asset Tracing": "Lawful asset research may review public corporate filings, property records, court documents and other accessible sources to develop leads for verification. We organize records, dates and source notes, distinguish leads from proven ownership, and do not access private accounts or guarantee recovery.",
   "Crypto Investigations": "Support may include public blockchain transaction review, transaction-ID preservation, wallet-flow timelines and organizing scam-related records for exchanges, authorities or qualified counsel. A wallet address alone does not establish identity, and tracing or recovery is never guaranteed."
  }
  service_text = service_notes.get(cat, "We can discuss lawful research, digital evidence organization or explicitly authorized security testing relevant to this topic. Work must be agreed in writing and comply with applicable law. No result or recovery is guaranteed.")
  body += "<h2>How Zenith Hackers can assist</h2><p>" + e(service_text) + "</p><h2>Why choose an evidence-led approach</h2><p>Ask any provider about written scope, lawful basis, methodology, confidentiality, data retention, reporting format, fees and limitations. A responsible team should never request passwords, seed phrases, private keys or one-time codes.</p>"
 else:
  body += "<h2>Discuss your situation</h2><p>Zenith Hackers can discuss whether lawful research, public-source analysis, digital evidence organization, public blockchain analysis or explicitly authorized security testing fits your situation. Any work should be agreed in writing and comply with applicable law. No result or asset recovery is guaranteed.</p>"
 canonical=base+"/blog/"+slug+"/"
 schema=json.dumps({"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"datePublished":date.today().isoformat(),"author":{"@type":"Organization","name":"Zenith Hackers"},"mainEntityOfPage":canonical})
 return """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>"""+e(title)+""" | Zenith Hackers</title><meta name="description" content=\""""+e(desc)+"""\"><link rel="canonical" href=\""""+canonical+"""\"><script type="application/ld+json">"""+schema+"""</script><style>body{margin:0;background:#0b1220;color:#e9eef8;font:17px/1.75 system-ui}header,main,footer{max-width:850px;margin:auto;padding:24px}a{color:#63e6be}header{border-bottom:1px solid #26334a}h1{font-size:clamp(2rem,5vw,3.3rem);line-height:1.15}h2{margin-top:2em;color:#a7f3d0}article{background:#111b2e;border:1px solid #26334a;border-radius:18px;padding:clamp(20px,4vw,42px)}.cta{background:#142c35;border:1px solid #2c7467;border-radius:14px;padding:22px;margin-top:28px}</style></head><body><header><a href="../../">ZENITH HACKERS · INTELLIGENCE</a><p><a href="../../">Home</a> / <a href="../../blog/">Blog</a> / """+e(cat)+"""</p></header><main><article><p><strong>"""+e(cat)+"""</strong> · Guide """+str(n)+"""</p><h1>"""+e(title)+"""</h1><p>"""+e(desc)+"""</p>"""+body+"""<div class="cta"><h2>Need help with a lawful investigation?</h2><p>Contact Zenith Hackers to discuss lawful research and authorized security work. Never send passwords, seed phrases, private keys or one-time codes.</p><p><a href="../../#contact">Request a consultation</a> · <a href="mailto:support@zenithhackers.com">support@zenithhackers.com</a></p></div></article><section class="public-comments"><h2>Public comments &amp; reviews</h2><p>Comments are public. Sign in with GitHub if prompted; please never post passwords, seed phrases or private keys.</p><script src="https://utteranc.es/client.js" repo="samuel2samwell-dot/How-to-hire-a-hackers-" issue-term="pathname" label="public-feedback" theme="github-dark" crossorigin="anonymous" async></script></section></main><footer><a href="/#contact">Contact</a> · <a href="/blog/">All articles</a> · Educational information only.</footer></body></html>"""
from pathlib import Path
blog=Path("blog");blog.mkdir(exist_ok=True); items=[];n=0
for cat,topics in cats.items():
 count=102 if cat=="Ethical Hacking" else (98 if cat=="Offshore Legal Topics" else 100)
 for i in range(count):
  n+=1;topic=topics[i%len(topics)];title=angles[(i//len(topics))%len(angles)]+": "+topic.title()+" — "+cat; sl=slug(title+" "+str(n))
  d=blog/sl;d.mkdir(parents=True,exist_ok=True);(d/"index.html").write_text(page(title,cat,topic,sl,n),encoding="utf-8")
  items.append({"title":title,"category":cat,"topic":topic,"slug":sl,"url":sl+"/","description":"Practical guidance on "+topic+", evidence quality, responsible research and privacy."})

# Additional section-specific series requested for the homepage. The original 1,000 guides above remain intact.
extra_series = {
 "Hire a Hacker": {
  "count": 1000,
  "topics": ["authorized penetration testing","web application security review","network security assessment","cloud configuration review","API security testing","identity and access review","vulnerability validation","red-team exercise planning","security remediation roadmap","penetration-test reporting","rules of engagement","safe test environments","responsible disclosure","multifactor authentication review","external attack-surface review","secure configuration testing","security regression testing","third-party security assessment","incident-readiness review","ethical hacker selection","data protection during testing","critical finding escalation","test evidence handling","post-remediation retesting","business risk prioritization"]
 },
 "Private Investigator": {
  "count": 1000,
  "topics": ["lawful digital evidence research","public-record investigation","online identity verification","case chronology building","open-source intelligence review","evidence preservation planning","business due diligence","fraud indicator documentation","investigation report writing","privacy-aware research","source reliability assessment","cross-border research coordination","digital impersonation research","document authenticity checks","missing-information analysis","investigator engagement planning","lawful background research","evidence corroboration","timeline inconsistency review","professional referral coordination","confidentiality safeguards","case scope definition","public profile verification","record retention planning","investigative limitations","responsible client communication"]
 },
 "News": {
  "count": 1500,
  "topics": ["ethical hacking trends","security advisory analysis","responsible vulnerability disclosure","phishing campaign indicators","data breach lessons","privacy and digital evidence","incident response readiness","ransomware prevention practices","cloud security misconfigurations","identity theft prevention","blockchain scam warnings","cybersecurity governance","software patch prioritization","supply-chain security","multifactor authentication adoption","digital forensics fundamentals","public blockchain transparency","online fraud reporting","security testing standards","AI-enabled scam awareness","account takeover prevention","small-business security","vendor risk management","security awareness programs","evidence preservation after scams","safe incident communications","data minimization practices","authorized penetration testing","regulatory reporting preparation","security metrics for leaders"]
 },
 "Asset Tracing": {
  "count": 900,
  "topics": ["public-record asset research","corporate ownership records","beneficial ownership leads","court record review","property record verification","business affiliation analysis","lawful asset intelligence","cross-border records research","source corroboration","asset timeline construction","entity name matching","ownership uncertainty assessment","fraud-related record preservation","due diligence workflows","public filing interpretation","asset research report writing","evidence chain documentation","professional recovery referrals","research scope planning","asset recovery expectation setting","corporate registry checks","legal process coordination","record freshness verification","transaction record organization","risk indicator analysis"]
 },
 "Crypto Investigations": {
  "count": 800,
  "topics": ["public blockchain transaction tracing","wallet address evidence","crypto scam documentation","transaction timeline analysis","exchange reporting preparation","cross-chain movement review","blockchain attribution limitations","wallet clustering caveats","transaction identifier preservation","token transfer analysis","bridge transaction review","crypto impersonation scams","fraud communications preservation","public ledger research","on-chain evidence snapshots","exchange compliance referrals","crypto recovery scam warnings","case chronology for digital assets","transaction fee interpretation","blockchain analytics quality checks","wallet label verification","lawful evidence sharing","crypto incident response","address reuse indicators","digital asset investigation reports"]
 }
}
extra_angles = [
 "A practical field guide","A responsible workflow","Questions to ask before starting",
 "Common pitfalls and safer alternatives","How to assess the evidence","A checklist for decision-makers",
 "What professionals should explain","A step-by-step planning guide","How to document findings",
 "A risk-based approach","How to protect privacy","What the records can establish",
 "How to prepare a useful report","A guide for organizations","A guide for individuals",
 "How to compare service providers","What to verify independently","A guide to scope and limitations",
 "How to plan next steps","A quality-control checklist","A guide to lawful assistance",
 "How to avoid unsupported conclusions","A guide to preserving context","What responsible practice looks like",
 "How to organize a case file","A guide to clear communication","How to evaluate uncertainty",
 "A guide to practical safeguards","What to discuss in a consultation","How to build a defensible timeline"
]
for cat, cfg in extra_series.items():
    topics = cfg["topics"]
    for i in range(cfg["count"]):
        n += 1
        topic = topics[i % len(topics)]
        angle = extra_angles[(i // len(topics)) % len(extra_angles)]
        cycle = i // (len(topics) * len(extra_angles))
        title = f"{angle}: {topic.title()} — {cat}" + (f" (Part {cycle + 2})" if cycle else "")
        sl = slug(title + " " + str(n))
        d = blog / sl
        d.mkdir(parents=True, exist_ok=True)
        d.joinpath("index.html").write_text(page(title, cat, topic, sl, n, include_service_guidance=True), encoding="utf-8")
        items.append({
          "title": title, "category": cat, "topic": topic, "slug": sl, "url": sl + "/",
          "description": f"Guidance on {topic}, lawful scope, evidence quality, privacy and practical next steps."
        })

(blog/"articles.json").write_text(json.dumps(items,ensure_ascii=False),encoding="utf-8")
options='<option value="Services">Services</option>'+"".join('<option>'+e(c)+'</option>' for c in list(cats) + list(extra_series))
(blog/"index.html").write_text("""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Blog | Zenith Hackers</title><meta name="description" content="Browse 6,200 guides on ethical hacking, investigations, news, asset tracing, crypto and privacy."><meta name="robots" content="index,follow"><link rel="canonical" href="https://samuel2samwell-dot.github.io/How-to-hire-a-hackers-/blog/"><style>body{margin:0;background:#0b1220;color:#e9eef8;font:16px/1.6 system-ui}header,main,footer{max-width:1100px;margin:auto;padding:24px}a{color:#63e6be}h1{font-size:clamp(2.5rem,6vw,4rem)}input,select,button{padding:12px;border-radius:9px;border:1px solid #35445c;background:#111b2e;color:white}.controls{display:flex;gap:10px;flex-wrap:wrap}.controls input{flex:1;min-width:220px}#results{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:26px 0}.card{padding:20px;background:#111b2e;border:1px solid #26334a;border-radius:14px}.pager{display:flex;gap:12px;justify-content:center}footer{color:#aab7ca}</style></head><body><header><a href="../" aria-label="Return to Zenith Hackers homepage">← Zenith Hackers home</a><h1>Insights & Guides</h1><p>6,200 educational articles across fifteen categories.</p></header><main><div class="controls"><input id="q" type="search" placeholder="Search articles"><select id="cat"><option value="">All categories</option>"""+options+"""</select></div><p id="count"></p><div id="results"></div><div class="pager"><button id="prev">Previous</button><span id="page"></span><button id="next">Next</button></div></main><footer>Educational information only. Contact <a href="mailto:support@zenithhackers.com">Zenith Hackers</a>. Never share passwords or crypto recovery phrases.</footer><script src="blog.js"></script></body></html>""",encoding="utf-8")
(blog/"blog.js").write_text("""(async function(){const data=await fetch('articles.json').then(r=>r.json());const q=document.querySelector('#q'),cat=document.querySelector('#cat'),res=document.querySelector('#results'),count=document.querySelector('#count'),label=document.querySelector('#page'),prev=document.querySelector('#prev'),next=document.querySelector('#next');const params=new URLSearchParams(window.location.search);const requestedCategory=params.get('category');if(requestedCategory&&Array.from(cat.options).some(o=>o.value===requestedCategory))cat.value=requestedCategory;let page=1;function render(){const term=q.value.trim().toLowerCase(),arr=data.filter(a=>(!cat.value||(cat.value==='Services'?['Hire a Hacker','Private Investigator','Asset Tracing','Crypto Investigations','Ethical Hacking','Private Investigation','Cybersecurity','Blockchain Intelligence'].includes(a.category):a.category===cat.value))&&(!term||(a.title+' '+a.category+' '+a.topic+' '+a.description).toLowerCase().includes(term))),pages=Math.max(1,Math.ceil(arr.length/18));page=Math.min(page,pages);res.innerHTML=arr.slice((page-1)*18,page*18).map(a=>'<article class="card"><small>'+a.category+'</small><h2><a href="'+a.url+'">'+a.title+'</a></h2><p>'+a.description+'</p><a href="'+a.url+'">Read guide →</a></article>').join('')||'<p>No matching articles.</p>';count.textContent=arr.length+' articles found';label.textContent='Page '+page+' of '+pages;prev.disabled=page<=1;next.disabled=page>=pages}q.addEventListener('input',()=>{page=1;render()});cat.addEventListener('change',()=>{page=1;render()});prev.onclick=()=>{page--;render();scrollTo(0,0)};next.onclick=()=>{page++;render();scrollTo(0,0)};render()})().catch(()=>document.querySelector('#results').textContent='Articles temporarily unavailable. Reload the page.')""",encoding="utf-8")
urls=[base+"/",base+"/blog/"]+[base+"/blog/"+a["slug"]+"/" for a in items]
# Keep the sitemap focused on canonical, indexable HTML pages: homepage, article library, and every article.
Path("sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join("  <url><loc>"+html.escape(u)+"</loc></url>" for u in urls)+"\n</urlset>\n",encoding="utf-8")
Path("robots.txt").write_text("User-agent: *\nAllow: /\nDisallow: /supabase/\nSitemap: "+base+"/sitemap.xml\n",encoding="utf-8")
print("Generated",len(items),"articles in",len(cats),"categories.")

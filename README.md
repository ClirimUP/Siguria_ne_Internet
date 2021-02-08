# Siguria_ne_Internet

SQL Injection eshte nje teknike qe fut malicious files ne SQL statements permes webpage input. Eshte nje nga tekinkat me te shpeshta per hacking ne web pages. 
Prandaj per parandalimin e SQL Injections kemi shkruar nje 'code' ne gjuhen programuse Python. Skripta e shkruar kryen teste te automatizuar te URL-ave te faqeve, ku tregon ne qofte se ato jane Vulnerable ose Not Vulnerable. 

Kodi perbehet nga dy pjese. Pjesa e pare eshte shtypja e linkut per testim, ku kthen nese linku eshte Vulnerable apo jo. Pjesa e dyte eshte post argumenti i cili perdoret per shtypjen e nje argumenti per testimin e nje skripte te PHP. 

Menyra e perdorimit pershrkuhet nga keto hapa:
1.  Testimi i URL
  1.1.  Duhet te behet Run Kodi.
  1.2.  Pasi te hapet interface(GUI), duhet te shtypni nje link(URL) valid te web faqes.
  1.3.  Shtypni butonin 'Testo'.
2.  Testimi i PHP Scripts
  2.1.  Duhet te behet Run Kodi.
  2.2.  Pasi te hapet interface(GUI), duhet te shtypni pathin, URL e PHP scripts.
  2.3.  Ne 'Post Arguments' duhet te shtypni post argumentin qe gjendet ne PHP scripten. 
  2.4.  Shtypni butonon 'Testo'.

Dy shembuj te testimit: 
1.  Ne shembullin e pare kemi tesuar linkun 'https://www.youtube.com/watch?v=Sv6dMFF_yts&list=RDhLQl3WQQoQ0&index=4' e nje muzike. Menyra e ekzetkutimit si eshte bere rrjedh keshtu: Kemi bere run kodin, pasi na eshte hapur faqja ne pjesen 'Shtyp URL per testim' kemi shtypur linkun e mesiperm, dhe pastaj kemi shtypur butonin 'Testo', ku rezultati na eshte shfaqur te pjesa e shtypjes se URL. Rezultati i shfaqur ishte qe faqja nuk eshte Vulnerable 'Not Vulnerable'. Kurse linku 'https://freecoursesites.net/' na eshte shfaqur qe eshte 'Vulnerable'

2. Ne shembullin e dyte kemi tesuar nje scripte te krijuar nga ne te quajtur 'vulnTest.php'. Ne kete rast duhet te shtojm edhe 'Post Arugments', ku ne rastin tone ishte 'userid' pasi qe vet e kemi definuar ne kodin e php scriptes. Pasi kemi shtypur butonin 'Testo' na eshte shfaqur qe shte Vulnerable. 

Pjesa e dyte e kodit ka qene kryesisht per testim te programit nese eshte duke funksionuar. Pjesa kreysore e programit eshte pjesa e pare e linqeve 'Shtyp URL per Testim:'.
Kodi i shrkuajtur eshte nje kod i thjesht qe demostron nje test te nje URL nese eshte Vulnerable. Por ekzistojne edhe menyra tjera te testimit te disa URL per nje her me disa Post Argumente, po ashtu ekziston edhe testimi i playloads te krijar nga ne. Ky projekt ngrit vedijen e qytetareve per te zbuluar nese linqet jane te rrezikshme apo te cenueshme ndaj integritetin dhe konfidencialitetin e tyre. 

"""Marca uma versão nova do app antes de enviar pro GitHub.
Uso: python3 publicar.py
Atualiza o número da versão no index.html, no version.json e no sw.js,
para o botão "Atualizar" aparecer no celular depois do deploy."""
import re,json,datetime
v=datetime.datetime.now().strftime('%Y.%m.%d-%H%M')
p='index.html';s=open(p,encoding='utf-8').read()
s=re.sub(r"const APP_VERSION='[^']*';",f"const APP_VERSION='{v}';",s,count=1);open(p,'w',encoding='utf-8').write(s)
json.dump({'v':v},open('version.json','w'))
w=open('sw.js',encoding='utf-8').read();w=re.sub(r"const V='[^']*';",f"const V='entregas-{v}';",w,count=1)
if "'version.json'" not in w: pass
open('sw.js','w',encoding='utf-8').write(w)
print('Versão',v)

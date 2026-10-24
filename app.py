import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Calm Focus", page_icon="🌙", layout="centered")
st.markdown("""<style>
#MainMenu, header, footer {visibility:hidden;}
.stApp {background:#0e1822;}
.block-container {padding-top:0.5rem; max-width:760px;}
</style>""", unsafe_allow_html=True)

HTML = r"""
<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300;6..72,400&display=swap" rel="stylesheet">
<style>
:root{--bg1:#0e1822;--bg2:#183044;--ink:#e7eef0;--mute:#8da3ad;--ring:#86bfae;--soft:#b9b6dc;--line:rgba(231,238,240,.12);--card:rgba(255,255,255,.04)}
*{box-sizing:border-box}
body{margin:0;font-family:system-ui,sans-serif;color:var(--ink);background:radial-gradient(120% 90% at 50% 0%,var(--bg2),var(--bg1) 70%);min-height:100vh}
.wrap{max-width:580px;margin:0 auto;padding:24px 18px 50px;text-align:center}
.nav{display:flex;justify-content:center;gap:4px;margin-bottom:26px;flex-wrap:wrap}
.nav button,.modes button{background:none;border:0;color:var(--mute);padding:9px 16px;border-radius:99px;cursor:pointer;font-size:14px}
.nav button.on,.modes button.on{background:rgba(134,191,174,.16);color:var(--ink)}
.modes{display:inline-flex;gap:4px;border:1px solid var(--line);border-radius:99px;padding:4px}
.panel{display:none}.panel.show{display:block}
.dial{position:relative;width:260px;height:260px;margin:28px auto 20px}
.glow{position:absolute;inset:24px;border-radius:50%;background:radial-gradient(circle,rgba(134,191,174,.22),transparent 70%)}
.running .glow{animation:breathe 8s ease-in-out infinite}
@keyframes breathe{0%,100%{transform:scale(.9);opacity:.6}50%{transform:scale(1.12);opacity:1}}
svg{position:absolute;inset:0;transform:rotate(-90deg)}
.trk{fill:none;stroke:var(--line);stroke-width:5}
.bar{fill:none;stroke:var(--ring);stroke-width:5;stroke-linecap:round;transition:stroke-dashoffset .9s linear,stroke .6s}
.brk .bar{stroke:var(--soft)}
.time{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.time b{font-family:Newsreader,Georgia,serif;font-weight:300;font-size:64px;letter-spacing:1px}
.time span{color:var(--mute);font-size:13px}
button.pill{background:none;border:1px solid var(--line);color:var(--ink);padding:11px 28px;border-radius:99px;font-size:15px;cursor:pointer;margin:0 4px;transition:.2s}
button.main{background:rgba(134,191,174,.18);border-color:rgba(134,191,174,.5)}
button.pill:hover{border-color:var(--ring)}
.msg{min-height:20px;color:var(--soft);font-size:14px;margin:14px 0}
.card{border:1px solid var(--line);background:var(--card);border-radius:18px;padding:18px;margin-top:16px;text-align:left}
label,h3{display:block;font-weight:400;font-size:13px;color:var(--mute);margin:0 0 10px}
input,select{background:rgba(255,255,255,.05);border:1px solid var(--line);color:var(--ink);border-radius:10px;padding:9px 11px;font-size:14px;font-family:inherit}
select option{background:#16293a}
.nums input{width:62px;text-align:center;margin:0 10px 0 4px}
.row{display:flex;gap:8px}.row input{flex:1}
.tip{margin-top:12px;font-size:14px;line-height:1.6;color:var(--ink)}
.task{display:flex;align-items:center;gap:10px;padding:12px 0;border-bottom:1px solid var(--line);flex-wrap:wrap}
.task:last-child{border:0}.task span{flex:1;min-width:120px}.task.done span{text-decoration:line-through;color:var(--mute)}
.task small{color:var(--mute);font-size:12px}
.task button{background:none;border:0;color:var(--mute);cursor:pointer;font-size:16px}
.task .tp{flex-basis:100%;font-size:13px;line-height:1.6;color:var(--soft)}
input[type=checkbox]{accent-color:#86bfae;width:17px;height:17px}
.chat{height:340px;overflow-y:auto;display:flex;flex-direction:column;gap:10px;padding:4px}
.b{max-width:85%;padding:10px 14px;border-radius:16px;font-size:14px;line-height:1.55;text-align:left}
.b.u{align-self:flex-end;background:rgba(134,191,174,.2)}
.b.a{align-self:flex-start;background:rgba(185,182,220,.14)}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin:12px 0}
.chips button{background:none;border:1px solid var(--line);color:var(--mute);border-radius:99px;padding:6px 12px;font-size:12px;cursor:pointer}
.stats{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats div{padding:18px 4px}.stats div+div{border-left:1px solid var(--line)}
.stats b{display:block;font-family:Newsreader,Georgia,serif;font-weight:300;font-size:34px}
.stats span{color:var(--mute);font-size:12px}
.week{display:flex;align-items:flex-end;justify-content:space-between;height:110px;gap:10px}
.col{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%}
.col i{display:block;width:100%;max-width:30px;border-radius:6px 6px 2px 2px;background:linear-gradient(var(--ring),rgba(134,191,174,.25));min-height:3px}
.col.today i{background:linear-gradient(var(--soft),rgba(185,182,220,.25))}
.col small{color:var(--mute);font-size:11px;margin-top:6px}
.dots{letter-spacing:6px;color:var(--ring);margin-top:8px}
</style>

<div class="wrap" id="app">
<div class="nav" id="nav">
 <button data-p="timer" class="on">Focus</button><button data-p="tasks">Tasks</button>
 <button data-p="buddy">Study Buddy</button><button data-p="prog">Progress</button>
</div>

<div class="panel show" id="p-timer">
 <div class="modes" id="modes">
  <button data-m="focus" class="on">Focus</button><button data-m="short">Short break</button><button data-m="long">Long break</button>
 </div>
 <div class="dial"><div class="glow"></div>
  <svg viewBox="0 0 280 280"><circle class="trk" cx="140" cy="140" r="128"/><circle class="bar" id="bar" cx="140" cy="140" r="128" stroke-dasharray="804.25" stroke-dashoffset="0"/></svg>
  <div class="time"><b id="t">25:00</b><span id="lbl">ready to focus</span></div>
 </div>
 <div><button class="pill main" id="go">Start</button><button class="pill" id="rst">Reset</button></div>
 <div class="msg" id="msg"></div>
 <div class="card"><label>Working on</label>
  <div class="row"><select id="cur" style="flex:1"></select><button class="pill" id="tipBtn" style="padding:9px 16px;margin:0">✨ Tips</button></div>
  <div class="tip" id="tip"></div></div>
 <div class="card"><label>Set your timers (minutes)</label>
  <div class="nums">Focus <input id="cf" type="number" min="1" max="180"> Short <input id="cs" type="number" min="1" max="60"> Long <input id="cl" type="number" min="1" max="120"></div></div>
</div>

<div class="panel" id="p-tasks">
 <div class="card" style="margin-top:0"><label>Add a task</label>
  <div class="row"><input id="newT" placeholder="e.g. Revise hysteresis chapter"><button class="pill main" id="addT" style="margin:0;padding:9px 18px">Add</button></div></div>
 <div class="card"><div id="list"></div></div>
</div>

<div class="panel" id="p-buddy">
 <div class="card" style="margin-top:0">
  <div class="chat" id="chat"></div>
  <div class="chips" id="chips">
   <button>Explain this simply</button><button>Quiz me on my task</button><button>I feel unmotivated</button><button>Make a study plan</button>
  </div>
  <div class="row"><input id="say" placeholder="Ask your study buddy..."><button class="pill main" id="send" style="margin:0;padding:9px 18px">Send</button></div>
 </div>
</div>

<div class="panel" id="p-prog">
 <div class="stats">
  <div><b id="sToday">0</b><span>sessions today</span></div>
  <div><b id="sStreak">0</b><span>day streak</span></div>
  <div><b id="sMin">0</b><span>focus min today</span></div>
 </div>
 <div class="card"><h3>Last 7 days (focus minutes)</h3><div class="week" id="week"></div></div>
 <div class="card"><label>Daily goal (sessions)</label><input id="goal" type="number" min="1" max="20" style="width:70px"><div class="dots" id="dots"></div></div>
 <div class="card"><label>AI key (free Gemini key from Google AI Studio, stored only in this browser)</label>
  <div class="row"><input id="key" type="password" placeholder="paste key here"><button class="pill" id="saveKey" style="margin:0;padding:9px 18px">Save</button></div>
  <div class="tip" id="keyMsg" style="color:var(--mute);font-size:12px"></div></div>
</div>
</div>

<script>
const KEY='calm_focus_v2', MODEL='gemini-2.0-flash';
let S={days:{},goal:4,cfg:{focus:25,short:5,long:15},tasks:[],cur:'',key:'',chat:[]};
try{Object.assign(S,JSON.parse(localStorage.getItem(KEY)||'{}'))}catch(e){}
let mode='focus',total=S.cfg.focus*60,left=total,endAt=null,tick=null;
const $=id=>document.getElementById(id);
const save=()=>{try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmt=t=>esc(t).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/\n/g,'<br>');
const dk=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const SYS="You are a warm, calm study buddy for a university physics student. Use simple English, be concise (under 150 words), practical and encouraging. Use short lists when helpful.";

/* ---------- AI ---------- */
async function ai(contents){
  if(!S.key) throw new Error('nokey');
  const r=await fetch('https://generativelanguage.googleapis.com/v1beta/models/'+MODEL+':generateContent?key='+encodeURIComponent(S.key),
   {method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({systemInstruction:{parts:[{text:SYS}]},contents})});
  const j=await r.json();
  if(!r.ok) throw new Error((j.error&&j.error.message)||'AI error');
  return j.candidates[0].content.parts.map(p=>p.text||'').join('');
}
const FALLBACK="**Simple plan**\n1. Write the exact goal of this session in one line.\n2. Remove distractions and keep your phone away.\n3. Work on one small part only.\n4. In the break, stand up, drink water, look far away.\n5. After the session, note what is finished.\n\n(Add a free AI key in Progress for tips made for your exact task.)";
async function tipFor(name,el){
  if(!name){el.innerHTML='Choose a task first.';return;}
  el.innerHTML='<span style="color:var(--mute)">thinking...</span>';
  try{const a=await ai([{role:'user',parts:[{text:'My task: "'+name+'". Give 4 short, practical steps to do it effectively using '+S.cfg.focus+'-minute focus sessions.'}]}]);
    el.innerHTML=fmt(a);}
  catch(e){el.innerHTML=fmt(e.message==='nokey'?FALLBACK:'AI problem: '+e.message);}
}

/* ---------- Timer ---------- */
function streak(){let n=0,d=new Date();if(!(S.days[dk(d)]||{}).s)d.setDate(d.getDate()-1);
  while((S.days[dk(d)]||{}).s){n++;d.setDate(d.getDate()-1)}return n;}
function render(){
  const m=Math.floor(left/60),s=left%60,txt=String(m).padStart(2,'0')+':'+String(s).padStart(2,'0');
  $('t').textContent=txt;document.title=txt+' · Calm Focus';
  $('bar').style.strokeDashoffset=804.25*(1-left/total);
  $('app').className='wrap '+(endAt?'running ':'')+(mode!=='focus'?'brk':'');
  $('go').textContent=endAt?'Pause':'Start';
  const t=S.days[dk(new Date())]||{s:0,m:0};
  $('sToday').textContent=t.s;$('sMin').textContent=t.m;$('sStreak').textContent=streak();
  let h='',mx=1,ds=[];
  for(let i=6;i>=0;i--){const d=new Date();d.setDate(d.getDate()-i);const v=(S.days[dk(d)]||{}).m||0;ds.push([d,v]);mx=Math.max(mx,v)}
  ds.forEach(([d,v],i)=>{h+='<div class="col '+(i==6?'today':'')+'"><i style="height:'+Math.max(3,v/mx*80)+'px" title="'+v+' min"></i><small>'+'SMTWTFS'[d.getDay()]+'</small></div>'});
  $('week').innerHTML=h;
  let dots='';for(let i=0;i<S.goal;i++)dots+=i<t.s?'●':'○';$('dots').textContent=dots;
}
function chime(){try{const c=new (window.AudioContext||window.webkitAudioContext)();
  [523,659,784].forEach((f,i)=>{const o=c.createOscillator(),g=c.createGain();o.frequency.value=f;o.connect(g);g.connect(c.destination);
  const t=c.currentTime+i*.35;g.gain.setValueAtTime(0,t);g.gain.linearRampToValueAtTime(.15,t+.05);g.gain.exponentialRampToValueAtTime(.001,t+1.2);o.start(t);o.stop(t+1.3)})}catch(e){}}
function stop(){clearInterval(tick);tick=null;endAt=null}
function setMode(m){mode=m;stop();total=S.cfg[m]*60;left=total;
  document.querySelectorAll('#modes button').forEach(b=>b.classList.toggle('on',b.dataset.m===m));
  $('lbl').textContent=m==='focus'?'ready to focus':'time to rest';render()}
function done(){stop();chime();
  if(mode==='focus'){const k=dk(new Date());const t=S.days[k]||{s:0,m:0};t.s++;t.m+=S.cfg.focus;S.days[k]=t;
    const tk=S.tasks.find(x=>x.id==S.cur);if(tk){tk.s++;tk.m+=S.cfg.focus}
    save();renderTasks();
    $('msg').textContent=t.s%4===0?'Lovely work. Take a long break.':'Session complete. Take a short break.';
    setMode(t.s%4===0?'long':'short')}
  else{$('msg').textContent='Break over. Ready when you are.';setMode('focus')}}
$('go').onclick=()=>{
  if(endAt){left=Math.max(0,Math.round((endAt-Date.now())/1000));stop();$('lbl').textContent='paused';render();return}
  $('msg').textContent='';endAt=Date.now()+left*1000;$('lbl').textContent=mode==='focus'?'stay with one thing':'breathe';
  tick=setInterval(()=>{left=Math.max(0,Math.round((endAt-Date.now())/1000));render();if(left<=0)done()},250);render()};
$('rst').onclick=()=>{$('msg').textContent='';setMode(mode)};
document.querySelectorAll('#modes button').forEach(b=>b.onclick=()=>{$('msg').textContent='';setMode(b.dataset.m)});
[['cf','focus'],['cs','short'],['cl','long']].forEach(([id,k])=>{
  $(id).value=S.cfg[k];
  $(id).onchange=e=>{S.cfg[k]=Math.min(180,Math.max(1,+e.target.value||S.cfg[k]));e.target.value=S.cfg[k];save();if(!endAt&&mode===k)setMode(k)}});
$('goal').value=S.goal;$('goal').onchange=e=>{S.goal=Math.min(20,Math.max(1,+e.target.value||4));save();render()};

/* ---------- Tasks ---------- */
function renderTasks(){
  $('cur').innerHTML='<option value="">- no task selected -</option>'+S.tasks.filter(x=>!x.done).map(x=>'<option value="'+x.id+'"'+(x.id==S.cur?' selected':'')+'>'+esc(x.t)+'</option>').join('');
  $('list').innerHTML=S.tasks.length?S.tasks.map(x=>'<div class="task '+(x.done?'done':'')+'" data-id="'+x.id+'"><input type="checkbox" '+(x.done?'checked':'')+'><span>'+esc(x.t)+'</span><small>'+x.s+' sessions · '+x.m+' min</small><button data-a="tip" title="AI tips">✨</button><button data-a="del" title="Delete">×</button><div class="tp"></div></div>').join(''):'<span style="color:var(--mute);font-size:14px">No tasks yet. Add your first one above.</span>';
}
function addTask(){const v=$('newT').value.trim();if(!v)return;S.tasks.push({id:Date.now(),t:v,done:false,s:0,m:0});$('newT').value='';save();renderTasks()}
$('addT').onclick=addTask;$('newT').onkeydown=e=>{if(e.key==='Enter')addTask()};
$('cur').onchange=e=>{S.cur=e.target.value;save()};
$('tipBtn').onclick=()=>{const tk=S.tasks.find(x=>x.id==S.cur);tipFor(tk&&tk.t,$('tip'))};
$('list').onclick=e=>{const row=e.target.closest('.task');if(!row)return;const tk=S.tasks.find(x=>x.id==row.dataset.id);
  if(e.target.type==='checkbox'){tk.done=e.target.checked;if(tk.done&&S.cur==tk.id)S.cur='';save();renderTasks()}
  else if(e.target.dataset.a==='del'){S.tasks=S.tasks.filter(x=>x!==tk);if(S.cur==tk.id)S.cur='';save();renderTasks()}
  else if(e.target.dataset.a==='tip'){tipFor(tk.t,row.querySelector('.tp'))}};

/* ---------- Study Buddy ---------- */
function renderChat(){
  const hi='Hi! I am your study buddy. Ask me to explain a topic, quiz you, or make a plan.';
  $('chat').innerHTML='<div class="b a">'+hi+'</div>'+S.chat.map(m=>'<div class="b '+(m.role==='user'?'u':'a')+'">'+fmt(m.parts[0].text)+'</div>').join('');
  $('chat').scrollTop=1e6}
async function sendChat(txt){
  txt=(txt||$('say').value).trim();if(!txt)return;$('say').value='';
  const tk=S.tasks.find(x=>x.id==S.cur);
  S.chat.push({role:'user',parts:[{text:txt+(tk?'\n(My current task: '+tk.t+')':'')}]});
  renderChat();$('chat').insertAdjacentHTML('beforeend','<div class="b a" id="th" style="color:var(--mute)">thinking...</div>');$('chat').scrollTop=1e6;
  let reply;try{reply=await ai(S.chat.slice(-10))}catch(e){reply=e.message==='nokey'?'I need a free AI key to chat. Add it in the Progress tab (Google AI Studio gives one for free).':'AI problem: '+e.message;S.chat.pop()}
  if(!(reply.startsWith('I need')||reply.startsWith('AI problem')))S.chat.push({role:'model',parts:[{text:reply}]});
  save();renderChat();
  if(reply.startsWith('I need')||reply.startsWith('AI problem'))$('chat').insertAdjacentHTML('beforeend','<div class="b a">'+esc(reply)+'</div>')}
$('send').onclick=()=>sendChat();$('say').onkeydown=e=>{if(e.key==='Enter')sendChat()};
document.querySelectorAll('#chips button').forEach(b=>b.onclick=()=>sendChat(b.textContent));

/* ---------- Key + tabs ---------- */
$('key').value=S.key;
$('saveKey').onclick=()=>{S.key=$('key').value.trim();save();$('keyMsg').textContent=S.key?'Saved in this browser only.':'Key removed.'};
document.querySelectorAll('#nav button').forEach(b=>b.onclick=()=>{
  document.querySelectorAll('#nav button').forEach(x=>x.classList.toggle('on',x===b));
  document.querySelectorAll('.panel').forEach(p=>p.classList.toggle('show',p.id==='p-'+b.dataset.p));});
renderTasks();renderChat();render();
</script>
"""
components.html(HTML, height=1000, scrolling=True)

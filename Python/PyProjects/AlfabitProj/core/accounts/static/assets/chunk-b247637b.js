import{a4 as oe,Z as J,i as q,j as Ne,a1 as De,a5 as xe,a6 as F,a7 as ce,a8 as Te,a9 as Be,V as qe,aa as Fe,ab as Ke,ac as He,ad as ze,t as Ve,B as m,J as Qe,K as Ye}from"./chunk-e8d35fff.js";import{D as Ce,a as K,o as Ze}from"./chunk-e33f88ff.js";import"./chunk-f868c71a.js";const Je=()=>({api:oe("api")}),We=()=>oe("pageContext");/*!
  * pinia v2.0.28
  * (c) 2022 Eduardo San Martin Morote
  * @license MIT
  */let we;const G=e=>we=e,Ee=Symbol();function re(e){return e&&typeof e=="object"&&Object.prototype.toString.call(e)==="[object Object]"&&typeof e.toJSON!="function"}var B;(function(e){e.direct="direct",e.patchObject="patch object",e.patchFunction="patch function"})(B||(B={}));function Bt(){const e=xe(!0),t=e.run(()=>q({}));let r=[],n=[];const s=J({install(o){G(s),s._a=o,o.provide(Ee,s),o.config.globalProperties.$pinia=s,n.forEach(c=>r.push(c)),n=[]},use(o){return!this._a&&!Be?n.push(o):r.push(o),this},_p:r,_a:null,_e:e,_s:new Map,state:t});return s}const ke=()=>{};function me(e,t,r,n=ke){e.push(t);const s=()=>{const o=e.indexOf(t);o>-1&&(e.splice(o,1),n())};return!r&&He()&&ze(s),s}function $(e,...t){e.slice().forEach(r=>{r(...t)})}function se(e,t){e instanceof Map&&t instanceof Map&&t.forEach((r,n)=>e.set(n,r)),e instanceof Set&&t instanceof Set&&t.forEach(e.add,e);for(const r in t){if(!t.hasOwnProperty(r))continue;const n=t[r],s=e[r];re(s)&&re(n)&&e.hasOwnProperty(r)&&!F(n)&&!ce(n)?e[r]=se(s,n):e[r]=n}return e}const Ge=Symbol();function Xe(e){return!re(e)||!e.hasOwnProperty(Ge)}const{assign:w}=Object;function et(e){return!!(F(e)&&e.effect)}function tt(e,t,r,n){const{state:s,actions:o,getters:c}=t,a=r.state.value[e];let u;function i(){a||(r.state.value[e]=s?s():{});const l=Ve(r.state.value[e]);return w(l,o,Object.keys(c||{}).reduce((h,d)=>(h[d]=J(m(()=>{G(r);const b=r._s.get(e);return c[d].call(b,b)})),h),{}))}return u=Oe(e,i,t,r,n,!0),u.$reset=function(){const h=s?s():{};this.$patch(d=>{w(d,h)})},u}function Oe(e,t,r={},n,s,o){let c;const a=w({actions:{}},r),u={deep:!0};let i,l,h=J([]),d=J([]),b;const _=n.state.value[e];!o&&!_&&(n.state.value[e]={}),q({});let A;function S(y){let f;i=l=!1,typeof y=="function"?(y(n.state.value[e]),f={type:B.patchFunction,storeId:e,events:b}):(se(n.state.value[e],y),f={type:B.patchObject,payload:y,storeId:e,events:b});const v=A=Symbol();qe().then(()=>{A===v&&(i=!0)}),l=!0,$(h,f,n.state.value[e])}const N=ke;function j(){c.stop(),h=[],d=[],n._s.delete(e)}function D(y,f){return function(){G(n);const v=Array.from(arguments),k=[],O=[];function ee(p){k.push(p)}function te(p){O.push(p)}$(d,{args:v,name:y,store:g,after:ee,onError:te});let T;try{T=f.apply(this&&this.$id===e?this:g,v)}catch(p){throw $(O,p),p}return T instanceof Promise?T.then(p=>($(k,p),p)).catch(p=>($(O,p),Promise.reject(p))):($(k,T),T)}}const H={_p:n,$id:e,$onAction:me.bind(null,d),$patch:S,$reset:N,$subscribe(y,f={}){const v=me(h,y,f.detached,()=>k()),k=c.run(()=>Ne(()=>n.state.value[e],O=>{(f.flush==="sync"?l:i)&&y({storeId:e,type:B.direct,events:b},O)},w({},u,f)));return v},$dispose:j},g=De(H);n._s.set(e,g);const E=n._e.run(()=>(c=xe(),c.run(()=>t())));for(const y in E){const f=E[y];if(F(f)&&!et(f)||ce(f))o||(_&&Xe(f)&&(F(f)?f.value=_[y]:se(f,_[y])),n.state.value[e][y]=f);else if(typeof f=="function"){const v=D(y,f);E[y]=v,a.actions[y]=f}}return w(g,E),w(Te(g),E),Object.defineProperty(g,"$state",{get:()=>n.state.value[e],set:y=>{S(f=>{w(f,y)})}}),n._p.forEach(y=>{w(g,c.run(()=>y({store:g,app:n._a,pinia:n,options:a})))}),_&&o&&r.hydrate&&r.hydrate(g.$state,_),i=!0,l=!0,g}function ae(e,t,r){let n,s;const o=typeof t=="function";typeof e=="string"?(n=e,s=o?r:t):(s=e,n=e.id);function c(a,u){const i=Fe();return a=a||i&&oe(Ee,null),a&&G(a),a=we,a._s.has(n)||(o?Oe(n,t,s,a):tt(n,s,a)),a._s.get(n)}return c.$id=n,c}function qt(e){{e=Te(e);const t={};for(const r in e){const n=e[r];(F(n)||ce(n))&&(t[r]=Ke(e,r))}return t}}const Ft=ae("exchange-store",{state:()=>({retryExchangeData:{sellAmount:"",sellRequisites:"",sellCountry:"",sellCity:"",buyAmount:"",buyRequisites:"",buyCountry:"",buyCity:"",checkbox:!1,email:""},urlMoneyDirection:{sellMoney:"",buyMoney:""},exchangeData:{sellMoney:{reqType:"",moneyType:"",prefix:"",i18Key:"",placeholder:""},buyMoney:{reqType:"",moneyType:"",prefix:"",i18Key:"",placeholder:""}}}),actions:{addUrlDirection(e){this.urlMoneyDirection=e},addExchangeData(e){this.exchangeData=e},addRetryExchangeData(e){const{sellMoney:t,buyMoney:r,...n}=e;this.addUrlDirection({sellMoney:t,buyMoney:r}),this.retryExchangeData=n},clearRetryExchangeData(){this.retryExchangeData={sellAmount:"",sellRequisites:"",sellCountry:"",sellCity:"",buyRequisites:"",buyCountry:"",buyCity:"",checkbox:!1,email:""}}},getters:{getUrlMoneyDirection:e=>{const t=Object.values(e.urlMoneyDirection).join("/");return t==="/"?"":t},getExchangeData:e=>e.exchangeData,getRetryExchangeData:e=>e.retryExchangeData}}),nt=(e,t=2)=>{if(!e)return"";const r=e.indexOf("@");if(!~r||t>r)return e;const[n,s]=e.split("@");return n.substring(0,t).padEnd(r,"*")+"@"+s};Ce.set({toExpPos:9e15});const Kt={install(e){e.config.globalProperties.$numTrimer=ie,e.config.globalProperties.$prettyNumber=M,e.config.globalProperties.$currencyType=P,e.config.globalProperties.$masker=rt,e.config.globalProperties.$clearStyleText=ot,e.config.globalProperties.$clearFroala=Ie,e.config.globalProperties.$getLastUpdateData=ct,e.config.globalProperties.$prettyPhone=Re,e.config.globalProperties.$prettyCard=Me,e.config.globalProperties.$prettyMoney=at,e.config.globalProperties.$exchangeMoneyParser=it}},M=(e,t={exp:20,decimalSeparator:"."})=>{const{exp:r=20,currency:n,decimalSeparator:s="."}=t,o=ie(e,r),c={maximumFractionDigits:r};let a;return n?["RUB","USD"].includes(n)?(c.currency=n,c.style="currency",a=new Intl.NumberFormat("ru-RU",c).format(o)):a=new Intl.NumberFormat("ru-RU").format(o)+" "+n:a=new Intl.NumberFormat("ru-RU",c).format(o),s!==","&&typeof a=="string"?a.replace(",",s):a},P=(e,t)=>e&&~e.indexOf("(")?e.match(/\((.*)\)/)[1]:t,U={7:{pattern:/7/},"#":{pattern:/[0-9]/},X:{pattern:/[0-9a-zA-Z]/},S:{pattern:/[a-zA-Z]/},A:{pattern:/[a-zA-Z]/,uppercase:!0},a:{pattern:/[a-zA-Z]/,lowercase:!0},"!":{escape:!0},"*":{repeat:!0},E:{pattern:/./}},rt=(e="",t,r=!0)=>{if(!t)return e;let n=0,s=0,o="",c="";for(;n<t.length&&s<e.length;){let a=t[n];const u=e[s],i=U[a];if(i&&i.pattern)i.pattern.test(u)&&(o+=st(u,i),n++,r&&t[n]&&(U[t[n]]?U[t[n]]&&U[t[n]].escape&&(o+=t[n+1],n=n+2):(o+=t[n],n++))),s++;else if(i&&i.repeat){const l=U[t[n-1]];l&&!l.pattern.test(u)?n++:n--}else i&&i.escape&&(n++,a=t[n]),r&&(o+=a),u===a&&s++,n++}for(;r&&n<t.length;){const a=t[n];if(U[a]){c="";break}c+=a,n++}return o+c},st=(e,t)=>(t.transform&&(e=t.transform(e)),t.uppercase?e.toLocaleUpperCase():t.lowercase?e.toLocaleLowerCase():e),Ie=e=>e.replace(/<p data-f-id="pbf".*<\/p>/g,""),ot=e=>(e=Ie(e),e.replace(/<strong\s*>.*<\/strong>/gm,"").replace(/style=['"](.*?)['"]/gm,"")),ct=e=>(e=e.replace(/<p data-f-id="pbf".*<\/p>/g,""),e.replace(/style=['"](.*?)['"]/gm,"").replace(/<br>/gm,"").match(/<strong\s*>.*<\/strong>/gm)),ie=(e,t=20)=>{if(!e||isNaN(+e))return e;let r=new Ce(e).toFixed(t).toString().replace(/[^0-9.,]/g,"").replace(",",".");const n=r.match(/[.,](.*)/);if(n&&n[1]){const s=r.indexOf(".");n[1].length>=t&&(r=r.slice(0,s+t+1))}return r},Re=e=>{const t=e==null?void 0:e.replace(/[^0-9]/g,""),r=(t==null?void 0:t.split("").splice(0,12))??[],n=r.splice(0,1).join(""),s=r.splice(0,3).join(""),o=r.splice(0,3).join(""),c=r.splice(0,2).join(""),a=r.splice(0,2).join("");let u="";return u+=n?"+"+n:"",u+=s?" ("+s:"",u+=o?") "+o:"",u+=c?"-"+c:"",u+=a?"-"+a:"",u},Me=e=>{if(!e)return"";const t=16,r=4,n=String(e).replace(/[^0-9]/g,"").slice(0,t),s=Math.floor(n.length/r);let o=n;if(s>=1){let c=[];for(let a=0;a<n.length;a+=r)c.push(n.slice(a,a+r));o=c.join(" ")}return o},at=(e,t)=>{const r=String(e).replace(/[^0-9.,]/g,"").replace(/[,]/g,".");let n="",s=!1;for(let o=0;o<r.length;o++){const c=r[o];if(c!=="."){n+=c;continue}c==="."&&!s&&o!==0&&(n+=c,s=!0)}return ie(n,t)||""},it=e=>{const t={reqType:"",moneyType:e.currency_type||"",prefix:P(e.code,e.bestchange_code),i18Key:"",placeholder:"",clearValue:""},r="^(7|38|77)\\(?([0-9]{3})\\)?[-.•]?([0-9]{3})[-.•]?([0-9]{4})$",n="^\\d{16}$";switch(e.re){case r:t.reqType="tel",t.i18Key="wallet {0}",t.placeholder="+7 (999) 999 - 99 - 99";break;case n:t.reqType="cc-number",t.i18Key="card_number {0}",t.placeholder="0000 0000 0000 0000";break;default:t.reqType="wallet",t.i18Key="address {0}",t.placeholder=e.exemple||""}return t},ue=["QWRUB","YAMRUB"],Ht=e=>{const{money1_currency_type:t,money1_bcode:r,money2_currency_type:n,money2_bcode:s}=e.value;function o(u,i){return ue.includes(u)?"PS":i==="FIAT"?"BANK":i}const c=o(r,t),a=o(s,n);return{orderDirection:`${c}-${a}`}},be=(e,t,r)=>{const n={requisites:[{title:"address",value:r||""}]};if(e==="FIAT")ue.includes(t)?n.requisites=t==="QWRUB"?[{title:"wallet",value:Re(r)}]:[{title:"wallet",value:r}]:t==="ACCRUB"?n.requisites=[{title:"account_number",value:r}]:n.requisites=[{title:"card_number",value:Me(r)}];else if(e==="CASH"){const s=(r==null?void 0:r.split(","))??[];if(s.length===3){const[o,c]=s,a=o==="[object Object]"?"Россия":o;n.requisites=[{title:"country",value:a,halfSize:!0},{title:"city",value:c,halfSize:!0}]}}return n},zt=(e,t)=>{var T,p,fe,ye,he,pe,de,ge;const r=(T=t==null?void 0:t.sell_currency)==null?void 0:T.currency_type,n=(p=t==null?void 0:t.sell_currency)==null?void 0:p.code,s=(fe=t==null?void 0:t.sell_currency)==null?void 0:fe.bestchange_code,o=(ye=t==null?void 0:t.buy_currency)==null?void 0:ye.currency_type,c=(he=t==null?void 0:t.buy_currency)==null?void 0:he.code,a=(pe=t==null?void 0:t.buy_currency)==null?void 0:pe.bestchange_code,u=(de=t==null?void 0:t.sell_currency)==null?void 0:de.exponent,i=(ge=t==null?void 0:t.buy_currency)==null?void 0:ge.exponent,{money1_currency_type:l,money1:h,money1_bcode:d,money2_currency_type:b,money2:_,money2_bcode:A}=e,S=l??r,N=h??n,j=d??s,D=b??o,H=_??c,g=A??a,E=ue.includes(j)?"PS":S==="FIAT"?"BANK":S,{reqKey:y,requisites:f}=be(S,j,e.req_money1),{reqKey:v,requisites:k}=be(D,g,e.req_money2),O=P(N,j),ee=P(H,g),te={sellReqKey:y,buyReqKey:v,sellRequisites:f,buyRequisites:k,sellMoneyType:S,sellMoneyPrefix:O,sellMoneyCode:j,buyMoneyType:D,buyMoneyPrefix:ee,buyMoneyCode:g,sellMoneyName:N,buyMoneyName:H,sellExponent:u,buyExponent:i};return{orderDirection:`${E}-${D}`,exchangeData:te}};let I=null,Y=null,Z=null;const Pe={baseURL:"https://alfabit.org/api/v1"},ut={baseURL:{}.VITE_CMS_HOST??"https://cms.alfabit.org/api"};let X;const lt=e=>{if(!e)return!0;try{let{exp:t}=Ze(e);return t*=1e3,Date.now()>=t}catch(t){return console.error(t),!0}},Ae=()=>{let e=!1,t=[];return{isRefreshing:e,failedQueue:t,processQueue:(n,s=null)=>{t.forEach(o=>{n?o.reject(n):o.resolve(s)}),t=[]}}},le=e=>{throw e},ft=()=>{let{failedQueue:e,isRefreshing:t,processQueue:r}=Ae();return async n=>{const s=n.config;return!s._retry&&n.response.status===403?t?new Promise((o,c)=>{e.push({resolve:o,reject:c})}).then(o=>(s.headers.Authorization=`Token ${o}`,K(s))).catch(o=>Promise.reject(o)):(s._retry=!0,t=!0,new Promise((o,c)=>{$e().post("/user/refresh",{refresh:X}).then(({access:a})=>{je().defaults.headers.Authorization=`Token ${a}`,s.headers.Authorization=`Token ${a}`,r(null,a),o(K(s))}).catch(a=>{r(a,null),c(a)}).finally(()=>{t=!1})})):Promise.reject(n)}},yt=()=>{let{failedQueue:e,isRefreshing:t,processQueue:r}=Ae();return n=>{var o;const s=((o=n.headers.Authorization)==null?void 0:o.replace("Token ",""))??"";return lt(s)?t?new Promise((c,a)=>{e.push({resolve:c,reject:a})}).then(c=>(n.headers.Authorization=`Token ${c}`,n)):(t=!0,new Promise((c,a)=>{$e().post("/user/refresh",{refresh:X}).then(({access:u})=>{je().defaults.headers.Authorization=`Token ${u}`,n.headers.Authorization=`Token ${u}`,r(null,u),c(n)}).catch(u=>{r(u,null),a(u)}).finally(()=>{t=!1})})):n}},ht=()=>(Y=K.create(Pe),Y.interceptors.response.use(({data:e})=>e,le),Y),pt=(e,t)=>{if(!I){const r={...Pe};e&&(r.headers={Authorization:`Token ${e}`}),X=t,I=K.create(r),I.interceptors.request.use(yt()),I.interceptors.response.use(n=>n,ft()),I.interceptors.response.use(({data:n})=>n,le)}return I},dt=()=>(Z=K.create(ut),Z.interceptors.response.use(({data:e})=>e,le),Z),gt=e=>{X=e},je=(e,t)=>I??pt(e,t),$e=()=>Y??ht(),Vt=()=>Z??dt(),Qt=ae("user",()=>{const{api:e}=Je(),{set:t,clear:r}=Rt(),n=q(null),s={ip:m(()=>{var i;return((i=n.value)==null?void 0:i.ip)??"-"}),uid:m(()=>{var i;return`UID: ${(i=n.value)==null?void 0:i.uid}`}),isEmailValidated:m(()=>{var i;return((i=n.value)==null?void 0:i.isEmailValidated)??!1}),email:m(()=>{var i;return(i=n.value)==null?void 0:i.email}),secureEmail:m(()=>{var i;return nt((i=n.value)==null?void 0:i.email)}),lastEntrance:m(()=>{var i;return((i=n.value)==null?void 0:i.lastEntrance)??"-"}),balance:m(()=>{var l;const i=(l=n.value)==null?void 0:l.balance;return i?M(i,{exp:2,currency:"RUB",decimalSeparator:","}):"-"}),referralId:m(()=>{var i;return((i=n.value)==null?void 0:i.referralId)??"-"})},o=async(i,l)=>{const{tokens:{refresh:h,access:d},username:b,rid:_,email:A,email_validated:S}=await e.AUTH.LOGIN({email:i,password:l});t(d,h),gt(h),u({name:b,email:A,referralId:_,isEmailValidated:S})},c=()=>{r(),n.value=null},a=async({username:i,password:l,password2:h,email:d})=>{await e.AUTH.REGISTER({username:i,password:l,password2:h,email:d})},u=async i=>{n.value=i};return{user:n,details:s,login:o,logout:c,register:a,loadDetails:u}});/*!
 * cookie
 * Copyright(c) 2012-2014 Roman Shtylman
 * Copyright(c) 2015 Douglas Christopher Wilson
 * MIT Licensed
 */var Ue=_t,_e=vt,mt=decodeURIComponent,bt=encodeURIComponent,z=/^[\u0009\u0020-\u007e\u0080-\u00ff]+$/;function _t(e,t){if(typeof e!="string")throw new TypeError("argument str must be a string");for(var r={},n=t||{},s=e.split(";"),o=n.decode||mt,c=0;c<s.length;c++){var a=s[c],u=a.indexOf("=");if(!(u<0)){var i=a.substring(0,u).trim();if(r[i]==null){var l=a.substring(u+1,a.length).trim();l[0]==='"'&&(l=l.slice(1,-1)),r[i]=St(l,o)}}}return r}function vt(e,t,r){var n=r||{},s=n.encode||bt;if(typeof s!="function")throw new TypeError("option encode is invalid");if(!z.test(e))throw new TypeError("argument name is invalid");var o=s(t);if(o&&!z.test(o))throw new TypeError("argument val is invalid");var c=e+"="+o;if(n.maxAge!=null){var a=n.maxAge-0;if(isNaN(a)||!isFinite(a))throw new TypeError("option maxAge is invalid");c+="; Max-Age="+Math.floor(a)}if(n.domain){if(!z.test(n.domain))throw new TypeError("option domain is invalid");c+="; Domain="+n.domain}if(n.path){if(!z.test(n.path))throw new TypeError("option path is invalid");c+="; Path="+n.path}if(n.expires){if(typeof n.expires.toUTCString!="function")throw new TypeError("option expires is invalid");c+="; Expires="+n.expires.toUTCString()}if(n.httpOnly&&(c+="; HttpOnly"),n.secure&&(c+="; Secure"),n.sameSite){var u=typeof n.sameSite=="string"?n.sameSite.toLowerCase():n.sameSite;switch(u){case!0:c+="; SameSite=Strict";break;case"lax":c+="; SameSite=Lax";break;case"strict":c+="; SameSite=Strict";break;case"none":c+="; SameSite=None";break;default:throw new TypeError("option sameSite is invalid")}}return c}function St(e,t){try{return t(e)}catch{return e}}function xt(){return typeof document=="object"&&typeof document.cookie=="string"}function Tt(e,t){return typeof e=="string"?Ue(e,t):typeof e=="object"&&e!==null?e:{}}function Ct(e,t){return typeof t>"u"&&(t=!e||e[0]!=="{"&&e[0]!=="["&&e[0]!=='"'),!t}function ve(e,t){t===void 0&&(t={});var r=wt(e);if(Ct(r,t.doNotParse))try{return JSON.parse(r)}catch{}return e}function wt(e){return e&&e[0]==="j"&&e[1]===":"?e.substr(2):e}var R=globalThis&&globalThis.__assign||function(){return R=Object.assign||function(e){for(var t,r=1,n=arguments.length;r<n;r++){t=arguments[r];for(var s in t)Object.prototype.hasOwnProperty.call(t,s)&&(e[s]=t[s])}return e},R.apply(this,arguments)},Et=function(){function e(t,r){var n=this;this.changeListeners=[],this.HAS_DOCUMENT_COOKIE=!1,this.cookies=Tt(t,r),new Promise(function(){n.HAS_DOCUMENT_COOKIE=xt()}).catch(function(){})}return e.prototype._updateBrowserValues=function(t){this.HAS_DOCUMENT_COOKIE&&(this.cookies=Ue(document.cookie,t))},e.prototype._emitChange=function(t){for(var r=0;r<this.changeListeners.length;++r)this.changeListeners[r](t)},e.prototype.get=function(t,r,n){return r===void 0&&(r={}),this._updateBrowserValues(n),ve(this.cookies[t],r)},e.prototype.getAll=function(t,r){t===void 0&&(t={}),this._updateBrowserValues(r);var n={};for(var s in this.cookies)n[s]=ve(this.cookies[s],t);return n},e.prototype.set=function(t,r,n){var s;typeof r=="object"&&(r=JSON.stringify(r)),this.cookies=R(R({},this.cookies),(s={},s[t]=r,s)),this.HAS_DOCUMENT_COOKIE&&(document.cookie=_e(t,r,n)),this._emitChange({name:t,value:r,options:n})},e.prototype.remove=function(t,r){var n=r=R(R({},r),{expires:new Date(1970,1,1,0,0,1),maxAge:0});this.cookies=R({},this.cookies),delete this.cookies[t],this.HAS_DOCUMENT_COOKIE&&(document.cookie=_e(t,"",n)),this._emitChange({name:t,value:void 0,options:r})},e.prototype.addChangeListener=function(t){this.changeListeners.push(t)},e.prototype.removeChangeListener=function(t){var r=this.changeListeners.indexOf(t);r>=0&&this.changeListeners.splice(r,1)},e}();const kt=Et,L=new kt,W=e=>e.substring(e.lastIndexOf(".",e.lastIndexOf(".")-1)+1),Ot={get(){return L.get("accessToken")},set(e,t=W(window==null?void 0:window.location.hostname)){L.set("accessToken",e,{path:"/",domain:t})},clear(e=W(window==null?void 0:window.location.hostname)){L.remove("accessToken",{path:"/",domain:e})}},It={get(){return L.get("refreshToken")},set(e,t=W(window==null?void 0:window.location.hostname)){L.set("refreshToken",e,{path:"/",domain:t})},clear(e=W(window==null?void 0:window.location.hostname)){L.remove("refreshToken",{path:"/",domain:e})}},V={accessToken:Ot,refreshToken:It},Rt=ae("tokens",()=>{const e=q(null),t=q(null),r=m(()=>!!e.value&&!!t.value);return{access:e,refresh:t,isLoggedIn:r,set:(o,c)=>{V.accessToken.set(o),V.refreshToken.set(c),e.value=o,t.value=c},clear:()=>{V.accessToken.clear(),V.refreshToken.clear(),e.value=null,t.value=null}}}),Mt=(e,t)=>`${M(e)} ${t}`,Le=(e,t,r,n)=>r?`1 ${P(n?t:e)} = ${M(r,{exp:6})} ${P(n?e:t)}`:null,Pt=({money1:e,money2:t,recalc_exchange_rate:r})=>Le(e,t,r),At=({money1:e,money2:t,exchange_rate:r,turn_the_course:n})=>Le(e,t,r,n),Q=(e,t)=>`${M(t)} ${P(e)}`,x={buy:{given_currency:{get:({money1:e})=>e,coin:{from:"money1_bcode"}},address:{from:"req_money1"},order_amount:{get:({money1:e,amount_money1:t})=>Q(e,t)}},sell:{received_currency:{get:({amount_money2:e,money2:t})=>Mt(e,t),coin:{from:"money2_bcode"}},wallet_address:{from:"req_money2"},order_amount:{get:({money2:e,amount_money2:t})=>Q(e,t)},txid:{get:({money2_link_blockchain:e})=>e&&e.split("/").pop()}},summary:{given_amount:{get:({money1:e,amount_in:t})=>Q(e,+t)},recalc_exchange_rate:{get:e=>Pt(e)},received_sum:{get:({money2:e,amount_money2:t})=>Q(e,t)}}},jt={"COIN-FIAT":{buy:{given_currency:x.buy.given_currency,replenishment_address:{from:"payment_number"},order_amount:x.buy.order_amount},sell:x.sell,summary:x.summary},"COIN-CASH":{buy:x.buy,sell:{received_currency:{get:({money2:e})=>e,coin:"CASHRUB"},wallet_address:x.sell.wallet_address,order_amount:x.sell.order_amount},summary:x.summary}},ne=(e,t)=>Object.entries(e).map(([r,n])=>{let s="";n.from&&(s=t[n.from]),n.get&&(s=n.get(t));const o={title:r,text:s};return n.coin&&(o.coin=t[n.coin.from]??""),o}).filter(r=>!!r.text),$t=(e,t)=>{const{buy:r,sell:n,summary:s}=jt[t]??x;return{buy:ne(r,e),sell:ne(n,e),summary:ne(s,e)}},Yt=(e,t)=>{const r=m(()=>$t(e.value,t.value));return{operationDetails:m(()=>{var s,o,c,a,u;return{number:e.value.id,rate:At(e.value),buyDetails:(s=r.value)==null?void 0:s.buy,sellDetails:(o=r.value)==null?void 0:o.sell,summaryDetails:(c=r.value)==null?void 0:c.summary,date:Qe(e.value.date_make_order*1e3).format("DD.MM.YYYY, HH:mm Z"),rawDate:e.value.date_make_order*1e3,registryLink:(((a=e.value)==null?void 0:a.money2_link_blockchain)??"")+(((u=e.value)==null?void 0:u.result)??"")}})}},{global:{t:C}}=Ye,Se={"PS-COIN":[{value:()=>C("pay_from_application")},{value:(e,t)=>t.device.isMobile?null:C("pay_from_mobile")}],"COIN-FIAT":[{title:C("amount_to_pay"),value:({amount_money1:e})=>M(e)},{title:C("payment_requisites"),value:({payment_number:e})=>e},{title:C("memo_tag"),value:({comment_in:e,view_comment:t})=>t?e:null}],DEFAULT:[{title:C("amount_to_pay"),value:({amount_money1:e})=>M(e)},{title:C("payment_requisites"),value:({payment_number:e})=>e},{title:C("message_for_receiver"),value:({comment_in:e,view_comment:t})=>t?e:null}]},Ut=(e,t,r)=>(Se[t]??Se.DEFAULT).map(s=>({title:s.title,value:s.value(e,r)})).filter(s=>!!s.value),Zt=(e,t)=>{const r=We();return{requisites:m(()=>Ut(e.value,t.value,r))}};export{kt as C,Me as a,V as b,Bt as c,je as d,$e as e,Kt as f,Vt as g,Qt as h,L as i,Rt as j,Ft as k,M as l,Je as m,zt as n,Yt as o,Re as p,Ht as q,Zt as r,qt as s,We as u};
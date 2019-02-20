(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{113:function(e,t,a){},115:function(e,t,a){},126:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),l=a(12),c=a.n(l),o=(a(77),a(16)),i=a(17),s=a(20),m=a(18),u=a(19),d=(a(79),a(130)),h=a(135),p=a(128),E=a(129),b=a(137),v=a(85),f=(a(81),a(132)),g=(a(83),function(e){return r.a.createElement("div",null,r.a.createElement(f.a,{method:"POST"},r.a.createElement(v.a,{type:"submit",name:"ledSwitch",variant:"danger",value:"red"},"Red"),r.a.createElement(v.a,{type:"submit",name:"ledSwitch",variant:"success",value:"green"},"Green"),r.a.createElement(v.a,{type:"submit",name:"ledSwitch",variant:"primary",value:"blue"},"Blue"),r.a.createElement(v.a,{type:"submit",name:"ledSwitch",variant:"secondary",value:"off"},"Off")))}),w=function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement(p.a,null,r.a.createElement(E.a,null,r.a.createElement("h2",null,"Welcome to IoT Web Controller"),r.a.createElement("p",null,"The Website is in Development.")),r.a.createElement("div",null,r.a.createElement("h2",null,"Development Testing Area"),r.a.createElement(b.a,{variant:"flush"},r.a.createElement(b.a.Item,null,r.a.createElement("input",{className:"spacing",type:"text"}),r.a.createElement(v.a,{className:"spacing",variant:"primary",type:"submit"},"Submit"),"Temperature"),r.a.createElement(b.a.Item,null,r.a.createElement(g,null),"LED Light Toggles",r.a.createElement("p",null,"My Token connection: ",window.token)),r.a.createElement(b.a.Item,null)))))}}]),t}(n.Component),O=(a(87),function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(p.a,{className:"contentPane"},r.a.createElement("div",{className:"headerlayout"},r.a.createElement("div",{className:"spacer"},r.a.createElement("h2",{className:"title"},"About "),r.a.createElement("p",null,"My Token connection: ",window.token),r.a.createElement("p",null,"The goal of this project is the research and development into current and future applications of IoT technology. Over the course of the Fall Semester we have researched current technologies and software used in IoT. We have considered various options and have mitigated our list then decided on the most appropriate task. "),r.a.createElement("p",null,"Our project aims to create a home IoT network utilizing the raspberry pi as a central server, various devices can be added to this network and accessed/controlled through a companion web application with the potential of expanding to other application platforms. "),r.a.createElement("p",null,"Our project aims to explore containerization for optimization, we have researched both Docker and Kubernetes as candidates. Various TCP options were investigated and support for existing devices will be a topic of research as progress is made. "))))}}]),t}(n.Component)),j=a(36),y=a(131),k=(a(89),function(e){function t(e,a){var n;return Object(o.a)(this,t),(n=Object(s.a)(this,Object(m.a)(t).call(this,e,a))).handleHide=n.handleHide.bind(Object(j.a)(Object(j.a)(n))),n.state={show:!1},n}return Object(u.a)(t,e),Object(i.a)(t,[{key:"handleHide",value:function(){this.setState({show:!1})}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"modal-container"},r.a.createElement(v.a,{bsStyle:"primary",bsSize:"medium",onClick:function(){return e.setState({show:!0})}},"+ Add Device"),r.a.createElement(y.a,{show:this.state.show,onHide:this.handleHide,container:this,"aria-labelledby":"contained-modal-title"},r.a.createElement(y.a.Header,{closeButton:!0},r.a.createElement(y.a.Title,{id:"contained-modal-title"},"Input The Device Settings")),r.a.createElement(y.a.Body,null,"ADD DEVICE CONTENT"),r.a.createElement(y.a.Footer,null,r.a.createElement(v.a,{onClick:this.handleHide},"Close"))))}}]),t}(r.a.Component)),T=(a(113),function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(p.a,{className:"contentPane"},r.a.createElement("div",{className:"headerlayout"},r.a.createElement("h2",{className:"title"},"Devices "),r.a.createElement("p",null,"My Token connection: ",window.token),r.a.createElement("div",{className:"spacer"}),r.a.createElement(k,null)),r.a.createElement(p.a,{className:"contentList"},r.a.createElement(b.a,null,r.a.createElement(b.a.Item,null,"LED 1"),r.a.createElement(b.a.Item,null,"LED 2"),r.a.createElement(b.a.Item,null,"Temperature 1"),r.a.createElement(b.a.Item,null,"Temperature 2"),r.a.createElement(b.a.Item,null,"Forecast"))))}}]),t}(n.Component)),I=a(133),C=a(136),N=a(134),S=(a(115),a(68)),D=a.n(S),x=function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(I.a,{bg:"light",expand:"lg"},r.a.createElement(I.a.Brand,{href:"/"},r.a.createElement("img",{className:"logo_image",src:D.a,alt:"logo"})," ","IoT Web Controller"),r.a.createElement(I.a.Toggle,{"aria-controls":"basic-navbar-nav"}),r.a.createElement(I.a.Collapse,{id:"basic-navbar-nav"},r.a.createElement(C.a,{className:"mr-auto"},r.a.createElement(C.a.Link,{href:"/about"},"About"),r.a.createElement(C.a.Link,{href:"/devices"},"Devices"),r.a.createElement(N.a,{title:"Account",id:"basic-nav-dropdown"},r.a.createElement(N.a.Item,{href:"https://github.com/BenjaminPalko/IoTHomeServer",target:"_blank"},"GitHub Source Code"),r.a.createElement(N.a.Item,{href:"/account/configuration"},"Configuration"),r.a.createElement(N.a.Item,{href:"/account/change_password"},"Change Password"),r.a.createElement(N.a.Divider,null),r.a.createElement(N.a.Item,{href:"/logging_out"},"Log Out"))),r.a.createElement(I.a.Text,null,"Signed in as: ",r.a.createElement("a",{href:"#login"},"Andrew Nguyen"))))}}]),t}(n.Component),H=function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(d.a,null,r.a.createElement("div",null,r.a.createElement(x,null),r.a.createElement(h.a,{exact:!0,path:"/",component:w}),r.a.createElement(h.a,{path:"/about",component:O}),r.a.createElement(h.a,{path:"/devices",component:T})))}}]),t}(n.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(r.a.createElement(H,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})},68:function(e,t,a){e.exports=a.p+"media/logo_body.bf7b2f69.svg"},72:function(e,t,a){e.exports=a(126)},77:function(e,t,a){},79:function(e,t,a){},81:function(e,t,a){},83:function(e,t,a){},87:function(e,t,a){},89:function(e,t,a){}},[[72,2,1]]]);
//# sourceMappingURL=main.0b28777c.chunk.js.map
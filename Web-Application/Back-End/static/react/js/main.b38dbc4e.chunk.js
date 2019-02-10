(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{110:function(e,t,a){},112:function(e,t,a){},123:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),c=a(12),l=a.n(c),o=(a(76),a(14)),i=a(15),s=a(18),m=a(16),u=a(17),d=(a(78),a(127)),h=a(131),p=a(125),E=a(126),b=a(132),f=a(83),v=(a(80),function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement(p.a,null,r.a.createElement(E.a,null,r.a.createElement("h2",null,"Welcome to IoT Web Controller"),r.a.createElement("p",null,"The Website is in Development."),r.a.createElement("p",null,"My Token connection: ",window.token)),r.a.createElement("div",null,r.a.createElement("h2",null,"Development Testing Area"),r.a.createElement(b.a,{variant:"flush"},r.a.createElement(b.a.Item,null,r.a.createElement(f.a,{variant:"primary"},"B"),r.a.createElement(f.a,{variant:"danger"},"R"),r.a.createElement(f.a,{variant:"warning"},"Y"),r.a.createElement(f.a,{className:"spacing",variant:"secondary"},"Off"),"LED Light Toggles"),r.a.createElement(b.a.Item,null,r.a.createElement("input",{className:"spacing",type:"text"}),r.a.createElement(f.a,{className:"spacing",variant:"primary",type:"submit"},"Submit"),"Temperature"),r.a.createElement(b.a.Item,null),r.a.createElement(b.a.Item,null)))))}}]),t}(n.Component)),g=(a(84),function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(p.a,{className:"contentPane"},r.a.createElement("div",{className:"headerlayout"},r.a.createElement("div",{className:"spacer"},r.a.createElement("h2",{className:"title"},"About "),r.a.createElement("p",null,"The goal of this project is the research and development into current and future applications of IoT technology. Over the course of the Fall Semester we have researched current technologies and software used in IoT. We have considered various options and have mitigated our list then decided on the most appropriate task. "),r.a.createElement("p",null,"Our project aims to create a home IoT network utilizing the raspberry pi as a central server, various devices can be added to this network and accessed/controlled through a companion web application with the potential of expanding to other application platforms. "),r.a.createElement("p",null,"Our project aims to explore containerization for optimization, we have researched both Docker and Kubernetes as candidates. Various TCP options were investigated and support for existing devices will be a topic of research as progress is made. "))))}}]),t}(n.Component)),O=a(34),j=a(128),w=(a(86),function(e){function t(e,a){var n;return Object(o.a)(this,t),(n=Object(s.a)(this,Object(m.a)(t).call(this,e,a))).handleHide=n.handleHide.bind(Object(O.a)(Object(O.a)(n))),n.state={show:!1},n}return Object(u.a)(t,e),Object(i.a)(t,[{key:"handleHide",value:function(){this.setState({show:!1})}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"modal-container"},r.a.createElement(f.a,{bsStyle:"primary",bsSize:"medium",onClick:function(){return e.setState({show:!0})}},"+ Add Device"),r.a.createElement(j.a,{show:this.state.show,onHide:this.handleHide,container:this,"aria-labelledby":"contained-modal-title"},r.a.createElement(j.a.Header,{closeButton:!0},r.a.createElement(j.a.Title,{id:"contained-modal-title"},"Input The Device Settings")),r.a.createElement(j.a.Body,null,"ADD DEVICE CONTENT"),r.a.createElement(j.a.Footer,null,r.a.createElement(f.a,{onClick:this.handleHide},"Close"))))}}]),t}(r.a.Component)),y=(a(110),function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(p.a,{className:"contentPane"},r.a.createElement("div",{className:"headerlayout"},r.a.createElement("h2",{className:"title"},"Devices "),r.a.createElement("div",{className:"spacer"}),r.a.createElement(w,null)),r.a.createElement(p.a,{className:"contentList"},r.a.createElement(b.a,null,r.a.createElement(b.a.Item,null,"LED 1"),r.a.createElement(b.a.Item,null,"LED 2"),r.a.createElement(b.a.Item,null,"Temperature 1"),r.a.createElement(b.a.Item,null,"Temperature 2"),r.a.createElement(b.a.Item,null,"Forecast"))))}}]),t}(n.Component)),k=a(129),I=a(133),T=a(130),C=(a(112),a(67)),N=a.n(C),D=function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(k.a,{bg:"light",expand:"lg"},r.a.createElement(k.a.Brand,{href:"/"},r.a.createElement("img",{className:"logo_image",src:N.a,alt:"logo"})," ","IoT Web Controller"),r.a.createElement(k.a.Toggle,{"aria-controls":"basic-navbar-nav"}),r.a.createElement(k.a.Collapse,{id:"basic-navbar-nav"},r.a.createElement(I.a,{className:"mr-auto"},r.a.createElement(I.a.Link,{href:"/about"},"About"),r.a.createElement(I.a.Link,{href:"/devices"},"Devices"),r.a.createElement(T.a,{title:"Account",id:"basic-nav-dropdown"},r.a.createElement(T.a.Item,{href:"https://github.com/BenjaminPalko/IoTHomeServer",target:"_blank"},"GitHub Source Code"),r.a.createElement(T.a.Item,{href:"/account/configuration"},"Configuration"),r.a.createElement(T.a.Item,{href:"/account/change_password"},"Change Password"),r.a.createElement(T.a.Divider,null),r.a.createElement(T.a.Item,{href:"/logging_out"},"Log Out"))),r.a.createElement(k.a.Text,null,"Signed in as: ",r.a.createElement("a",{href:"#login"},"Andrew Nguyen"))))}}]),t}(n.Component),S=function(e){function t(){return Object(o.a)(this,t),Object(s.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return r.a.createElement(d.a,null,r.a.createElement("div",null,r.a.createElement(D,null),r.a.createElement(h.a,{exact:!0,path:"/",component:v}),r.a.createElement(h.a,{path:"/about",component:g}),r.a.createElement(h.a,{path:"/devices",component:y})))}}]),t}(n.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));l.a.render(r.a.createElement(S,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})},67:function(e,t,a){e.exports=a.p+"media/logo_body.bf7b2f69.svg"},71:function(e,t,a){e.exports=a(123)},76:function(e,t,a){},78:function(e,t,a){},80:function(e,t,a){},84:function(e,t,a){},86:function(e,t,a){}},[[71,2,1]]]);
//# sourceMappingURL=main.b38dbc4e.chunk.js.map
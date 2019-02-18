(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{113:function(e,a,t){},115:function(e,a,t){},126:function(e,a,t){"use strict";t.r(a);var n=t(0),r=t.n(n),l=t(12),c=t.n(l),o=(t(77),t(16)),i=t(17),m=t(19),s=t(18),u=t(20),d=(t(79),t(130)),h=t(135),p=t(128),E=t(129),b=t(137),f=t(85),v=(t(81),t(132)),g=(t(83),function(e){return r.a.createElement("div",null,r.a.createElement(v.a,{method:"POST"},r.a.createElement(v.a.Group,{controlId:"formBasicEmail"},r.a.createElement(v.a.Label,null,"Email address"),r.a.createElement(v.a.Control,{type:"email",placeholder:"Enter email"}),r.a.createElement(v.a.Text,{className:"text-muted"},"We'll never share your email with anyone else.")),r.a.createElement(v.a.Group,{controlId:"formBasicPassword"},r.a.createElement(v.a.Label,null,"Password"),r.a.createElement(v.a.Control,{name:"passwordName",type:"password",placeholder:"Password"})),r.a.createElement(v.a.Group,{controlId:"formBasicChecbox"},r.a.createElement(v.a.Check,{type:"checkbox",label:"Check me out"})),r.a.createElement(f.a,{name:"red-led",variant:"primary"},"Red"),r.a.createElement(f.a,{name:"green-led",variant:"primary"},"Green"),r.a.createElement(f.a,{name:"blue-led",variant:"primary"},"Blue"),r.a.createElement(f.a,{name:"off-led",variant:"primary"},"Off"),r.a.createElement(f.a,{variant:"primary",type:"submit"},"Submit")))}),w=function(e){function a(){return Object(o.a)(this,a),Object(m.a)(this,Object(s.a)(a).apply(this,arguments))}return Object(u.a)(a,e),Object(i.a)(a,[{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement(p.a,null,r.a.createElement(E.a,null,r.a.createElement("h2",null,"Welcome to IoT Web Controller"),r.a.createElement("p",null,"The Website is in Development."),r.a.createElement("p",null,"My Token connection: ",window.token)),r.a.createElement("div",null,r.a.createElement("h2",null,"Development Testing Area"),r.a.createElement(b.a,{variant:"flush"},r.a.createElement(b.a.Item,null,r.a.createElement(f.a,{variant:"primary"},"B"),r.a.createElement(f.a,{variant:"danger"},"R"),r.a.createElement(f.a,{variant:"warning"},"Y"),r.a.createElement(f.a,{className:"spacing",variant:"secondary"},"Off"),"LED Light Toggles"),r.a.createElement(b.a.Item,null,r.a.createElement("input",{className:"spacing",type:"text"}),r.a.createElement(f.a,{className:"spacing",variant:"primary",type:"submit"},"Submit"),"Temperature"),r.a.createElement(b.a.Item,null,r.a.createElement(g,null)),r.a.createElement(b.a.Item,null)))))}}]),a}(n.Component),y=(t(87),function(e){function a(){return Object(o.a)(this,a),Object(m.a)(this,Object(s.a)(a).apply(this,arguments))}return Object(u.a)(a,e),Object(i.a)(a,[{key:"render",value:function(){return r.a.createElement(p.a,{className:"contentPane"},r.a.createElement("div",{className:"headerlayout"},r.a.createElement("div",{className:"spacer"},r.a.createElement("h2",{className:"title"},"About "),r.a.createElement("p",null,"My Token connection: ",window.token),r.a.createElement("p",null,"The goal of this project is the research and development into current and future applications of IoT technology. Over the course of the Fall Semester we have researched current technologies and software used in IoT. We have considered various options and have mitigated our list then decided on the most appropriate task. "),r.a.createElement("p",null,"Our project aims to create a home IoT network utilizing the raspberry pi as a central server, various devices can be added to this network and accessed/controlled through a companion web application with the potential of expanding to other application platforms. "),r.a.createElement("p",null,"Our project aims to explore containerization for optimization, we have researched both Docker and Kubernetes as candidates. Various TCP options were investigated and support for existing devices will be a topic of research as progress is made. "))))}}]),a}(n.Component)),O=t(36),j=t(131),k=(t(89),function(e){function a(e,t){var n;return Object(o.a)(this,a),(n=Object(m.a)(this,Object(s.a)(a).call(this,e,t))).handleHide=n.handleHide.bind(Object(O.a)(Object(O.a)(n))),n.state={show:!1},n}return Object(u.a)(a,e),Object(i.a)(a,[{key:"handleHide",value:function(){this.setState({show:!1})}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"modal-container"},r.a.createElement(f.a,{bsStyle:"primary",bsSize:"medium",onClick:function(){return e.setState({show:!0})}},"+ Add Device"),r.a.createElement(j.a,{show:this.state.show,onHide:this.handleHide,container:this,"aria-labelledby":"contained-modal-title"},r.a.createElement(j.a.Header,{closeButton:!0},r.a.createElement(j.a.Title,{id:"contained-modal-title"},"Input The Device Settings")),r.a.createElement(j.a.Body,null,"ADD DEVICE CONTENT"),r.a.createElement(j.a.Footer,null,r.a.createElement(f.a,{onClick:this.handleHide},"Close"))))}}]),a}(r.a.Component)),I=(t(113),function(e){function a(){return Object(o.a)(this,a),Object(m.a)(this,Object(s.a)(a).apply(this,arguments))}return Object(u.a)(a,e),Object(i.a)(a,[{key:"render",value:function(){return r.a.createElement(p.a,{className:"contentPane"},r.a.createElement("div",{className:"headerlayout"},r.a.createElement("h2",{className:"title"},"Devices "),r.a.createElement("p",null,"My Token connection: ",window.token),r.a.createElement("div",{className:"spacer"}),r.a.createElement(k,null)),r.a.createElement(p.a,{className:"contentList"},r.a.createElement(b.a,null,r.a.createElement(b.a.Item,null,"LED 1"),r.a.createElement(b.a.Item,null,"LED 2"),r.a.createElement(b.a.Item,null,"Temperature 1"),r.a.createElement(b.a.Item,null,"Temperature 2"),r.a.createElement(b.a.Item,null,"Forecast"))))}}]),a}(n.Component)),T=t(133),C=t(136),N=t(134),D=(t(115),t(68)),x=t.n(D),S=function(e){function a(){return Object(o.a)(this,a),Object(m.a)(this,Object(s.a)(a).apply(this,arguments))}return Object(u.a)(a,e),Object(i.a)(a,[{key:"render",value:function(){return r.a.createElement(T.a,{bg:"light",expand:"lg"},r.a.createElement(T.a.Brand,{href:"/"},r.a.createElement("img",{className:"logo_image",src:x.a,alt:"logo"})," ","IoT Web Controller"),r.a.createElement(T.a.Toggle,{"aria-controls":"basic-navbar-nav"}),r.a.createElement(T.a.Collapse,{id:"basic-navbar-nav"},r.a.createElement(C.a,{className:"mr-auto"},r.a.createElement(C.a.Link,{href:"/about"},"About"),r.a.createElement(C.a.Link,{href:"/devices"},"Devices"),r.a.createElement(N.a,{title:"Account",id:"basic-nav-dropdown"},r.a.createElement(N.a.Item,{href:"https://github.com/BenjaminPalko/IoTHomeServer",target:"_blank"},"GitHub Source Code"),r.a.createElement(N.a.Item,{href:"/account/configuration"},"Configuration"),r.a.createElement(N.a.Item,{href:"/account/change_password"},"Change Password"),r.a.createElement(N.a.Divider,null),r.a.createElement(N.a.Item,{href:"/logging_out"},"Log Out"))),r.a.createElement(T.a.Text,null,"Signed in as: ",r.a.createElement("a",{href:"#login"},"Andrew Nguyen"))))}}]),a}(n.Component),B=function(e){function a(){return Object(o.a)(this,a),Object(m.a)(this,Object(s.a)(a).apply(this,arguments))}return Object(u.a)(a,e),Object(i.a)(a,[{key:"render",value:function(){return r.a.createElement(d.a,null,r.a.createElement("div",null,r.a.createElement(S,null),r.a.createElement(h.a,{exact:!0,path:"/",component:w}),r.a.createElement(h.a,{path:"/about",component:y}),r.a.createElement(h.a,{path:"/devices",component:I})))}}]),a}(n.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(r.a.createElement(B,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})},68:function(e,a,t){e.exports=t.p+"media/logo_body.bf7b2f69.svg"},72:function(e,a,t){e.exports=t(126)},77:function(e,a,t){},79:function(e,a,t){},81:function(e,a,t){},83:function(e,a,t){},87:function(e,a,t){},89:function(e,a,t){}},[[72,2,1]]]);
//# sourceMappingURL=main.3908bc4e.chunk.js.map
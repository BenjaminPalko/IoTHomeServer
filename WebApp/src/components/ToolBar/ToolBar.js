import React from 'react';

import logo from '../../logo_body.svg';
import DrawerToggleButton from '../SideDrawer/DrawerToggleButton';
import './ToolBar.css';


const toolbar = (props) => (
    <header className="toolbar">
        <nav className="toolbar_navigation">
            <div className="toolbar_toggle-button">
                <DrawerToggleButton click={props.drawerClickHandler}/>
            </div>
            <div className="toolbar_logo"><a href="/"><img className="logo_image" src={logo} alt="logo"/></a></div>
            <div className="logo_name">IOT Controller</div>
            <div className="spacer"/>

            <div className="toolbar_navigation-items">
                <ul>
                    <li><a href="/">IoT Device Library </a></li>
                    <li><a href="/">Raspberry Pi Console </a></li>
                    <li><a href="/">Notifications </a></li>
                    <li><a href="/">Control Settings </a></li>
                    <li><a href="/">Log Out </a></li>
                </ul>
            </div>
        </nav>
    </header>
);

export default toolbar;
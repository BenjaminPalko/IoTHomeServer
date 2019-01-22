import React from 'react';

import logo from '../../logo_body.svg';
import './SideDrawer.css';

const sideDrawer = props => {
    let drawerClasses = 'side-drawer';
    if(props.show) {
        drawerClasses = 'side-drawer open';
    }
    return (
        <nav className={drawerClasses}>
            <ul>
                <li><img className="logo_image_sideBar" src={logo} alt="logo"/></li>
                <li><a href="/">IoT Device Library </a></li>
                <li><a href="/">Raspberry Pi Console </a></li>
                <li><a href="/">Notifications </a></li>
                <li><a href="/">Control Settings </a></li>
                <li><a href="/">Log Out </a></li>
            </ul>
        </nav>
    );
};

export default sideDrawer;
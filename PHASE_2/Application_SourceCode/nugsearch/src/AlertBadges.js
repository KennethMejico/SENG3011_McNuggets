import React from 'react';
import './AlertBadges.css'

class AlertBadges extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            alerts: []
        };
    }

    componentDidMount() {
        fetch('/getAlerts').then(res => res.json()).then(data => {
            this.setState({alerts: data.alerts});
        })
    }

    navigateToPage(event) {
        console.log(event.target.dataset.alertname);
    }

    AlertBadge(alert) {
        return (
            <div className="AlertBadge" key={alert} data-alertname={alert} onClick={this.navigateToPage}>
                <p>OUTBREAK OF {alert.toUpperCase()}</p>
                <p>COULD LEAD TO LOCKDOWN</p>
            </div>
        );
    }

    render() {
        return (
            <div className="AlertBadgeArea">
                {Object.keys(this.state.alerts).map((alert) => (
                    this.AlertBadge(this.state.alerts[alert])
                ))}
            </div>
        )
    }
}

export default AlertBadges;
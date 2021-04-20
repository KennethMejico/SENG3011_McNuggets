import React from 'react'
import MyTable from './Table.js'
import BottomNav from './BottomNav.js'


import { withRouter } from 'react-router-dom';

const columns = [
          {
            id: 0,
            Header: "Event Date",
            accessor: "show.event_date"
          },
          {
            id: 1,
            Header: "Locations",
            accessor: "show.locations"
          },
          {
            id: 2,
            Header: "Diseases",
            accessor: "show.diseases"
          },
          {
            id: 3,
            Header: "Article Headline",
            accessor: "show.articleHeadline"
          },
          {
            id: 4,
            Header: "Article Link",
            accessor: "show.articleUrl",
            Cell: e =><a href={e.value}> {e.value} </a>
          }
    ];

class ResultsTable extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            data: this.processData()
        }
    }

    onlyUnique(value, index, self) {
        return self.indexOf(value) === index;
    }

    processData() {
        var results = this.props.location.state.data.results;
        var rows = [];
        for (const articleId in results) {
            var article = results[articleId];
            for (const reportId in article.reports) {
                var report = article["reports"][reportId];
                rows.push({
                    "show": {
                        "event_date": report.event_date.substring(0, 10),
                        "locations": report.locations.filter(this.onlyUnique).join(", "),
                        "diseases": report.diseases,
                        "articleHeadline": article.headline,
                        "articleUrl": article.url
                    }
                });
            }
        }
        return rows;
    }

    render() {
        return(
        <div>
            <div className="ResultBackground">
                <h2>Reports Between {this.props.location.state.startDate} and {this.props.location.state.endDate}</h2>
                <MyTable columns={columns} data={this.state.data} />
                <p />
                <BottomNav location={this.props.location}/>
                {/*<Link to={{
                    pathname: '/map',
                    state: {
                        data: this.props.location.state.data,
                        startDate: this.props.location.state.startDate,
                        endDate: this.props.location.state.endDate,
                    }
                }}>See Map</Link>*/}
            </div>
        </div>
        )
    }
}

export default withRouter(ResultsTable);

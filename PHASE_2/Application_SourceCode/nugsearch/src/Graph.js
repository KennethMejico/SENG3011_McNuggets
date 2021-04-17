import React from 'react'
import './Graph.css'
import { ResponsiveLine } from '@nivo/line'

import { withRouter } from 'react-router-dom';


class Graph extends React.Component {
    constructor(props) {
        super(props);
        console.log(this.props);
        this.state = {
            data: this.processData()
        }
        this.changeData = this.changeData.bind(this);
    }

    processData() {
      var data = [];
      var diseases = {};
      var results = this.props.location.state.data.results;
      var minDate;
      var maxDate;
      var toInsert;
      for (var articleId in results) { // articles for SourDough, response (I think) for us, results for bugsfree
        var article = results[articleId];
        for (const reportId in article.reports) {
          var report = article["reports"][reportId]

          var reportDate = new Date(report.event_date);
          console.log(minDate);
          console.log(maxDate);
          if (minDate) {
            if (reportDate < minDate) {
              minDate = reportDate;
            }
          } else {
            minDate = reportDate;
          }
          if (maxDate) {
            if (reportDate > maxDate) {
              maxDate = reportDate;
            }
          } else {
            maxDate = reportDate;
          }

          if (report["diseases"].length === 0) {
            if (diseases.other) {
              if (!this.incrementDate(report.event_date, diseases.other.data)) {
                toInsert = {
                    "x": report.event_date.substring(0, 10),
                    "y": 1
                  }
                this.insertDate(report.event_date, toInsert, diseases.other.data);
                // diseases.other.data.push({
                //   "x": report.event_date.substring(0, 10),
                //   "y": 1
                // })
              }
            } else {
              console.log("hit");
              diseases.other = {
                "data": [
                  {
                    "x": report.event_date.substring(0, 10),
                    "y": 1
                  }
                ],
              }
            }
          } else {
            for (const diseaseId in report.diseases) {
              var disease = report["diseases"][diseaseId];
              if (diseases[disease]) {
                if (!this.incrementDate(report.event_date, diseases[disease].data)) {
                  toInsert = {
                    "x": report.event_date.substring(0, 10),
                    "y": 1
                  }
                  this.insertDate(report.event_date, toInsert, diseases[disease].data);
                  // diseases[disease].data.push({
                  //   "x": report.event_date.substring(0, 10),
                  //   "y": 1
                  // })
                }
              } else {
                diseases[disease] = {
                  "data": [
                    {
                      "x": report.event_date.substring(0, 10),
                      "y": 1
                    }
                  ],
                }
              }
            }
          }
        }
      }

      var start = new Date(this.props.location.state.startDate);
      var end = new Date(this.props.location.state.endDate);
      // var start = minDate;
      // var end = maxDate;
      for (var date = start; date <= end; date.setDate(date.getDate() + 1)) {
        for (const diseaseName in diseases) {
          if (!this.hasDate(date.toISOString(), diseases[diseaseName]["data"])) {
            toInsert = {
              "x": date.toISOString().substring(0, 10),
              "y": 0
            }
            this.insertDate(date, toInsert, diseases[diseaseName].data);
            // diseases[diseaseName].data.push({
            //   "x": date.toISOString().substring(0, 10),
            //   "y": 0
            // })
          }
        }
      }

      for (const diseaseName in diseases) {
        data.push({
          "id": diseaseName,
          "data": diseases[diseaseName]["data"]
        })
      }

      console.log(data)
      return data
    }

    incrementDate(date, data) {
      var target = date.substring(0, 10);
      for (const i in data) {
        var dataPoint = data[i];
        if (dataPoint.x === target) {
          dataPoint.y += 1;
          return true;
        }
      }
      return false;
    }

    hasDate(date, data) {
      var target = date.substring(0, 10);
      for (const i in data) {
        var dataPoint = data[i];
        if (dataPoint.x === target) {
          return true;
        }
      }
      return false;
    }

    insertDate(date, toInsert, data) {
      var targetDate = new Date(date);
      for (const i in data) {
        var dataPoint = data[i];
        var d = new Date(dataPoint.x);
        if (d > targetDate) {
          data.splice(i, 0, toInsert);
          return;
        }
      }
      data.push(toInsert);
    }

    changeData(data) {
      console.log("change hit")
      this.setState({data: data}, () => {
        console.log(this.state.data);
      })
    }

    render() {
        return(
        <div>
            <div className="ResultBackground">
                <h2>Graph: COVID19 Results in World Between {this.props.location.state.startDate} and {this.props.location.state.endDate}</h2>
                {/* <img src={graphImage} alt="img" class="GraphImage"/> */}
                <ResponsiveLine
                    data={this.state.data}
                    margin={{ top: 50, right: 150, bottom: 100, left: 60 }}
                    xScale={{ type: 'point' }}
                    yScale={{ type: 'linear', min: 'auto', max: 'auto', stacked: false, reverse: false }}
                    curve="monotoneX"
                    axisTop={null}
                    axisRight={null}
                    axisBottom={{
                        orient: 'bottom',
                        tickSize: 5,
                        tickPadding: 5,
                        tickRotation: 0,
                        legend: 'Date',
                        legendOffset: 36,
                        legendPosition: 'middle'
                    }}
                    axisLeft={{
                        orient: 'left',
                        tickSize: 5,
                        tickPadding: 5,
                        tickRotation: 0,
                        legend: 'New Cases',
                        legendOffset: -40,
                        legendPosition: 'middle',
                        fontColor: 'white',
                    }}
                    pointSize={10}
                    pointColor={{ theme: 'background' }}
                    pointBorderWidth={2}
                    pointBorderColor={{ from: 'serieColor' }}
                    pointLabelYOffset={-12}
                    useMesh={true}
                    legends={[
                        {
                            anchor: 'bottom-right',
                            direction: 'column',
                            justify: false,
                            translateX: 100,
                            translateY: 0,
                            itemsSpacing: 0,
                            itemDirection: 'left-to-right',
                            itemWidth: 80,
                            itemHeight: 20,
                            itemOpacity: 0.75,
                            symbolSize: 12,
                            symbolShape: 'circle',
                            symbolBorderColor: 'rgba(0, 0, 0, .5)',
                            effects: [
                                {
                                    on: 'hover',
                                    style: {
                                        itemBackground: 'rgba(0, 0, 0, .03)',
                                        itemOpacity: 1
                                    }
                                }
                            ]
                        }
                    ]}
                    theme={theme}
                />
                <p />
                <a href="/map">See Map</a>
            </div>
        </div>
        )
    }
}

export default withRouter(Graph);

const theme = {
    axis: {
        fontSize: "14px",
        tickColor: "#eee",
        ticks: {
            line: {
                stroke: "#555555"
            },
            text: {
                fill: "#ffffff"
            }
        },
        legend: {
            text: {
                fill: "#ffffff"
            }
        }
    },
    legends: {
      text: {
        fill: "#ffffff"
      }
    }
}
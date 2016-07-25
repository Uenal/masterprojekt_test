var React = require('react')
  , Arrow3D = require('../shared/Arrow3D')
  , Graph = require('../shared/Graph')
  , TestNew = require('../shared/TestNew')
  , rabbit = require('../../js/rabbit')
  , DynamoArrow = require('../shared/DynamoArrow')
  , DynamoGraph = require('../shared/DynamoGraph')
  , TopBar = require('../shared/TopBar')
  , CanvasPos = require('../shared/CanvasPos')
  , Bluebird = require('bluebird')
  , request = require('superagent');

var EditSensor = require('./EditSensor')
  , DeleteSensor = require('./DeleteSensor');

var SingleSensor = React.createClass({

  propTypes: {
    user: React.PropTypes.object,
    sensor: React.PropTypes.object,
    allSensors : React.PropTypes.array
  },

  getInitialState: function() {
    return {
      robots: [],
      labyrinth: false,
      robot:  null,
      isLive: false,
      connection: {},
      cQ: [0, 0, 0, 0],
      cA: null,
      fields: [
        ['id', 'ID'],
        ['location', 'Location'],
        ['creationDate', 'Creation Date'],
        ['types','Sensor Types'],
        ['owner', 'Owner'],
        ['attachedGateway', 'Attached Gateway'],
        ['attachedCluster', 'Attached Cluster']
      ],
      data: [],
      editSensor: false,
      deleteSensor: false
    };
  },

  componentDidMount: function() {
    
    //Ist der Sensor vom Typ: "Labyrinth", werden alle Sensoren gesucht die den selben Typ haben.(this.state.robots) Damit diese von der RabbitMQ abboniert werden können.
    for(var x = 0; x < this.props.sensor.types.length; x++){

        if(this.props.sensor.types[x] == 'labyrinth' || this.props.sensor.types[x] == 'Labyrinth'){
            
            this.state.labyrinth = true;
        }
    }
    
    if(this.state.labyrinth == true){
        
        for(var i = 0; i < this.props.allSensors.length; i++){

            for(var j = 0; j < this.props.allSensors[i].types.length; j++){

                if(this.props.allSensors[i].types[j] == "labyrinth" || this.props.allSensors[i].types[j] == "Labyrinth"){

                    this.state.robots.push(this.props.allSensors[i]);
                }
            }
        }   
    }
  },

  handleSwitch: function() {
    var isLive = !this.state.isLive;
    console.log('is it live:', isLive);
    if (isLive) {
      var connection = this.connect();
        console.log(this);
    } else {
      this.disconnect();
    }
    this.setState({isLive: isLive, connection: connection});
  },

  test: function(body) {
    if (this.state.myInterval) clearInterval(this.state.myInterval);
    var that = this;
    var max = body.length
    var hz = Math.floor(1000/max) - 2;
    var i = 0;

    this.setState({data: body}, function() {
        
      var myInterval = setInterval(function() {
        if (i++ == max - 1) {
          i = 0;
          clearInterval(myInterval);
          return;
        }
        if (!that.state.data[i]) return;
        var date = that.state.data[i].time;
        var maxDate = that.state.data[that.state.data.length - 1].time;
        that.setState({
          robot:  that.state.data[i],
          cQ: that.state.data[i].orientation,
          cA: {value: that.state.data[i].acceleration, time: date},
          maxDate: {time: maxDate},
          myInterval: myInterval
        });
      }, hz);
    });
  },
    
  test2: function(body) {
   
      this.setState({
          robot:  body[0]
      });
  },

  connect: function() {
    
      if(this.state.labyrinth == false){
        
        var that = this;
        var rabbitClient = rabbit.connect();
        rabbitClient.connect('guest', 'guest', function() {
          var subscription = rabbitClient
            .subscribe('/exchange/friss_exch/'+that.props.sensor.id, function(msg) {

               //console.log(JSON.parse(msg.body));
               that.test(JSON.parse(msg.body));
          });
        });
        return rabbitClient;
      } else if(this.state.labyrinth == true){
          
        var that = this;      
        var rabbitClient = rabbit.connect();
        rabbitClient.connect('guest', 'guest', function() {
               
            for(var i = 0; i < that.state.robots.length; i++){
                var id = that.state.robots[i].id;
                
                rabbitClient
                .subscribe('/exchange/friss_exch/' + id, function(msg) {

                   that.test2(JSON.parse(msg.body));
                });
            }
            
        });
        return rabbitClient;
      }
  },

  disconnect: function() {
    this.state.connection.disconnect(function() {
      console.log('disconnect');
    });
  },

  renderFields: function(){
    var that = this;
    return this.state.fields.map(function(field){
      var value;
      var caption;
      var id;
      if(Array.isArray(field)){
        id = field[0];
        value = that.props.sensor[field[0]] || 'missing';
        caption = field[1];
      }else{
        value = that.props.sensor[field] || 'missing';
        caption = field;
        id = field;
      }
      var text = value;
      if(id === 'creationDate'){
        var date = new Date(text);
        text = date.toUTCString();
      }else if(id === 'types'){
        text = that.props.sensor[field[0]].join(', ');
      }
      return(
        <tr key={caption}>
          <td>{caption}</td>
          <td>{id === 'owner' ? <a href={"/user/" + text}>{text}</a> : text}</td>
        </tr>
      );
    });
  },

  //renderGraph: function(){
    //return (
      //<div className='row'>
        //<div className='large-12 columns' style={{border: '1px solid black',height:300}}>super meger krasse d3 Grafik</div>
      //</div>);
  //},

  handleEditSensor: function(){
    this.setState({editSensor: !this.state.editSensor})
  },

  handleDeleteSensor: function(){
    this.setState({deleteSensor: !this.state.deleteSensor});
  },

  render: function() {
      
    var displayStyle = this.state.editSensor || this.state.deleteSensor
                        ? 'block' : 'none';
    return (
      <div>
        <TopBar user={this.props.user} activePage='sensors' />
        <div style={{marginTop: 25}}>
          <div className='row column' style={{float: 'none'}}>
            <div className='callout'>
              <div className='row' style={{marginRight: 0}}>
                <div className='small-8 columns'>
                  <h3>{this.props.sensor.name}</h3>
                </div>
                <div className='small-4 columns' style={{textAlign: 'right', paddingRight: 0}}>
                  <div className='button' onClick={this.handleEditSensor}>
                    Edit
                  </div>
                  <div className='button alert'
                    style={{marginRight:0}}
                    onClick={this.handleDeleteSensor}>
                    Delete
                  </div>
                </div>
              </div>
                <table style={{width: '100%'}}>
                  <tbody style={{borderWidth: 0}}>
                    {this.renderFields()}
                  </tbody>
                </table>
            </div>
          </div>
          <div className='row column' style={{float:'none'}}>
            <div className='callout'>
              <div style={{textAlign: 'center'}}>
                <p style={{marginBottom: 0}}>Show Live Data</p>
                <div className="switch large">
                  <input className="switch-input"
                    id="yes-no"
                    type="checkbox"
                    onClick={this.handleSwitch}
                    name="exampleSwitch"/>
                  <label className="switch-paddle" htmlFor="yes-no">
                    <span className="show-for-sr"></span>
                    <span className="switch-active" aria-hidden="true">Yes</span>
                    <span className="switch-inactive" aria-hidden="true">No</span>
                  </label>
                </div>
              </div>
              <div className='row'>

                <div className='large-6 columns'>
                  <h5>Orientation</h5>
                  { this.state.isLive
                    ? <Arrow3D quad={this.state.cQ}/>
                    : <DynamoArrow />
                  }
                </div>
                <div className='large-6 columns'>
                  <h5>Acceleration</h5>
                  { this.state.isLive
                    ? <TestNew value={this.state.cA} maxDate={this.state.maxDate}/>
                    : <DynamoGraph />
                  }
                </div>

                <div className='large-15 columns'>
                    <CanvasPos value={this.state.robot} sensorType={this.props.sensor.types}/>
                </div>
              </div>
            </div>
          </div>
        </div>
        {this.state.editSensor
          ? <EditSensor cancelCallback={this.handleEditSensor}
            sensor={this.props.sensor}/>
          : null}
        {this.state.deleteSensor ? <DeleteSensor cancelCallback={this.handleDeleteSensor} sensor={this.props.sensor}/> : null}
          <div className='background-area'
            style={{display: displayStyle}}>
          </div>
      </div>
    );
  }
});

module.exports = SingleSensor;
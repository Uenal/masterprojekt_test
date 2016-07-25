var React = require('react');
var ReactDOM = require('react-dom');
var ReactUpdates = require("react/lib/ReactUpdates");

var CanvasPos = React.createClass({
    
  propTypes: {
	   value: React.PropTypes.object,
	   sensorType: React.PropTypes.array
  },

  getInitialState: function() {
      
      canvasContext = {};
      robots = [];
      canvas = <div></div>;
      text = <div></div>;
      //Test Robots.
      return{objects: [{name:'robot1',x:50,y:50,rad:20,color:['#f5ff00','#ff0000']},{name:'robot2',x:100,y:100,rad:20,color:['#1d00ff','#f5ff00']}, {name:'robot3',x:150,y:150,rad:20,color:['#097b00']},{name:'robot4',x:300,y:300,rad:20,color:['#A6A938','#00fff5']}]}
  },
    
  componentWillReceiveProps: function(next) {

      if (next.value === null) return;
      
          if(robots.length == 0){
              
              var c = new Circle(next.value.name, next.value.x ,next.value.y ,next.value.rad, next.value.color, canvasContext, next.value.rotation);
              robots.push(c);
          }

          if(!containsObject(next.value, robots)){
            
              var c2 = new Circle(next.value.name, next.value.x , next.value.y, next.value.rad,next.value.color,canvasContext, next.value.rotation);
              robots.push(c2);
          }
      
          
          for(var i= 0; i < robots.length; i++){
             
            if(robots[i].name == next.value.name){
                // Die PixyCam liefert uns einen maximalen Pixelwert von 150x150, da unser Canvas 500x500 Pixel ist, haben wir die X und die Y koordinate mit 10/3 multipliziert.
                robots[i].rotation = next.value.rotation;
                robots[i].x = next.value.x * (10/3);
                robots[i].y = next.value.y * (10/3);
            }
          }
  },
    
  componentDidMount: function() {
        
        if(containsObject2("Labyrinth", this.props.sensorType) || containsObject2("labyrinth", this.props.sensorType)){
            
                
            canvasContext = ReactDOM.findDOMNode(this.refs.myCanvas).getContext('2d');

            //Set the Canvas size.
            canvasContext.canvas.width = 500;    
            canvasContext.canvas.height = 500;

            // Push the available Objects in the CircleArray and set the Objects on the Canvas(For Random Test with Robots.)
            //    for(var i= 0; i < this.state.objects.length; i++){
            //        
            //        var c = new Circle(this.state.objects[i].x,this.state.objects[i].y, this.state.objects[i].rad,this.state.objects[i].color,canvasContext);
            //        circles.push(c);
            //        circles[i].draw(canvasContext);
            //    }
            this.update();
        }
  },
    
  update: function() {
     
      setInterval(function() {
          
        canvasContext.clearRect(0,0,500,500);
        for(var i= 0; i < robots.length; i++){
            
            robots[i].draw(canvasContext);
        }
      }, 1);
  },

  render: function() {
      
       if(containsObject2("Labyrinth", this.props.sensorType) || containsObject2("labyrinth", this.props.sensorType)){
            
            text = <h5>Labyrinth</h5>;
            canvas = <canvas id='myCanvass' ref="myCanvas"  style={{ backgroundImage: 'url(' + '../../img/maze.png' + ')' , width: 500, height: 500}}>  </canvas>;
        }else {
            
            canvas = <div></div>;
        }
    return (
        <div>
            <p>{this.props.value}</p>
            {text}
            {canvas}
        </div>
    );
  }
});

module.exports = CanvasPos;

function Circle(name, x, y, rad, color, ctx, rotation) {
     
    var _this = this;

    // constructor
    (function() {
        _this.name = name || 'unknown'
        _this.x = x  * (10/3)|| 0;
        _this.y = y  * (10/3)|| 0;
        _this.radius = rad || 20;
        _this.rotation = rotation || 0;
        _this.color = color || '#000000';
    })();

    this.draw = function(ctx) {

        test = 90;
        if(_this.color.length == 1){
            ctx.save();
            ctx.beginPath();
            ctx.translate(_this.x,_this.y);
            ctx.rotate(_this.rotation*Math.PI/180);
            ctx.arc(0, 0, _this.radius, 0, 2*Math.PI);
            ctx.fillStyle = _this.color[0];
            ctx.fill();
            ctx.closePath();
            
            ctx.beginPath();
//            ctx.rotate(test*Math.PI/180);
            ctx.moveTo(0,0);
            ctx.lineTo(0+27,0);
            ctx.lineWidth=2;
            ctx.stroke();
            ctx.closePath();
            ctx.restore();
            
        }
        
        if(_this.color.length == 2){
            ctx.save();
            ctx.beginPath();
            ctx.translate(_this.x,_this.y);
            ctx.rotate(_this.rotation*Math.PI/180);
            ctx.arc(0, 0, _this.radius, 0, Math.PI,true);
            ctx.fillStyle = _this.color[0];
            ctx.fill();
            ctx.closePath();

            ctx.beginPath();
            ctx.arc(0, 0, _this.radius, 0, Math.PI,false);
            ctx.fillStyle = _this.color[1];
            ctx.fill();
            ctx.closePath();
            
            ctx.beginPath();
            ctx.moveTo(0,0);
            ctx.lineTo(0+27,0);
            ctx.lineWidth=2;
            ctx.stroke();
            ctx.closePath();
            ctx.restore();
        }
    }
}

function containsObject(obj, list) {
    var i;
    for (i = 0; i < list.length; i++) {
        if (list[i].name === obj.name) {
            return true;
        }
    }

    return false;
}

function containsObject2(obj, list) {
    var i;
    for (i = 0; i < list.length; i++) {
        if (list[i] === obj) {
            return true;
        }
    }

    return false;
}
.cube3d-container {
	-webkit-perspective: 1000px;
	-moz-perspective: 1000px;
	-o-perspective: 1000px;
	-ms-perspective: 1000px;
	perspective: 1000px;

	-webkit-perspective-origin: 50%;
	-moz-perspective-origin: 50%;
	-moz-transform-origin: 50%;
	-o-perspective-origin: 50%;
	-ms-perspective-origin: 50%;
	perspective-origin: 50%;
	padding: 25px;
}


.cube3d-container .cube3d {
	color: #FFF;
	float: left;
	margin: 5px;

	height: {{ cube_size }}px;
	width: {{ cube_size }}px;
	-webkit-transition: -webkit-transform 0.5s ease;
	-moz-transition: -moz-transform 0.5s ease;
	-o-transition: -o-transform 0.5s ease;
	-ms-transition: -ms-transform 0.5s ease;
	transition: transform 0.5s ease;
	-webkit-transform-style: preserve-3d;
	-moz-transform-style: preserve-3d;
	-o-transform-style: preserve-3d;
	-ms-transform-style: preserve-3d;
	transform-style: preserve-3d;
	-webkit-transform-origin: 50%;
	-moz-transform-origin: 50%;
	-ms-transform-origin: 50%;
	-o-transform-origin: 50%;
	transform-origin: 50%;
}

.cube3d-container .cube3d .side {
      position: absolute;
      height: 100%;
      width: 100%;

      background: #eeeeee;
      background: -moz-linear-gradient(top, #eeeeee 0%, #CCCCCC 100%);
      background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #eeeeee), color-stop(100%, #CCCCCC));
      background: -webkit-linear-gradient(top, #eeeeee 0%, #CCCCCC 100%);
      background: -o-linear-gradient(top, #eeeeee 0%, #CCCCCC 100%);
      background: -ms-linear-gradient(top, #eeeeee 0%, #CCCCCC 100%);
      background: linear-gradient(to bottom, #eeeeee 0%, #CCCCCC 100%);
      filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#eeeeee', endColorstr='#CCCCCC',GradientType=0 );
}

.cube3d-container .cube3d .side:nth-child(1) {
	-webkit-transform: translateZ({% widthratio cube_size 2 1 %}px);
	-moz-transform: translateZ({% widthratio cube_size 2 1 %}px);
	-o-transform: translateZ({% widthratio cube_size 2 1 %}px);
	-ms-transform: translateZ({% widthratio cube_size 2 1 %}px);
	transform: translateZ({% widthratio cube_size 2 1 %}px);
}

.cube3d-container .cube3d .side:nth-child(2) {
	-webkit-transform: rotateY(90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-moz-transform: rotateY(90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-o-transform: rotateY(90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-ms-transform: rotateY(90deg) translateZ({% widthratio cube_size 2 1 %}px);
	transform: rotateY(90deg) translateZ({% widthratio cube_size 2 1 %}px);
}

.cube3d-container .cube3d .side:nth-child(3) {
	-webkit-transform: rotateY(180deg) translateZ({% widthratio cube_size 2 1 %}px);
	-moz-transform: rotateY(180deg) translateZ({% widthratio cube_size 2 1 %}px);
	-o-transform: rotateY(180deg) translateZ({% widthratio cube_size 2 1 %}px);
	-ms-transform: rotateY(180deg) translateZ({% widthratio cube_size 2 1 %}px);
	transform: rotateY(180deg) translateZ({% widthratio cube_size 2 1 %}px);
}

.cube3d-container .cube3d .side:nth-child(4) {
	-webkit-transform: rotateY(-90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-moz-transform: rotateY(-90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-o-transform: rotateY(-90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-ms-transform: rotateY(-90deg) translateZ({% widthratio cube_size 2 1 %}px);
	transform: rotateY(-90deg) translateZ({% widthratio cube_size 2 1 %}px);
}

.cube3d-container .cube3d .side:nth-child(5) {
	-webkit-transform: rotateX(-90deg) translateZ({% widthratio cube_size 2 1 %}px) rotate(180deg);
	-moz-transform: rotateX(-90deg) translateZ({% widthratio cube_size 2 1 %}px) rotate(180deg);
	-o-transform: rotateX(-90deg) translateZ({% widthratio cube_size 2 1 %}px) rotate(180deg);
	-ms-transform: rotateX(-90deg) translateZ({% widthratio cube_size 2 1 %}px) rotate(180deg);
	transform: rotateX(-90deg) translateZ({% widthratio cube_size 2 1 %}px) rotate(180deg);
}

.cube3d-container .cube3d .side:nth-child(6) {
	-webkit-transform: rotateX(90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-moz-transform: rotateX(90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-o-transform: rotateX(90deg) translateZ({% widthratio cube_size 2 1 %}px);
	-ms-transform: rotateX(90deg) translateZ({% widthratio cube_size 2 1 %}px);
	transform: rotateX(90deg) translateZ({% widthratio cube_size 2 1 %}px);
}

.clearfix {
	*zoom: 1
}

.clearfix:before {
	content: " ";
	display: table;
}

.clearfix:after {
	content: " "
	display: table
	clear: both
}

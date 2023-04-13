<template>
    <div class="container-fluid no-mp">
      <div class="row no-mp">
        <div class="col no-mp">
            <h2>About GeorgeBot</h2>
            <p>GeorgeBot is a ground based robot that utilizes a light detection and ranging (LiDAR)
            camera system to map indoor spaces.
            Architects and interior designers often need to create a virtual model
            of an existing room for remodeling or redesigning.
            Using GeorgeBot, this potentially tedious process can
            be automated, saving time for the designer.
            Additionally, in case of an emergency or counter-intelligence situation,
            GeorgeBot can be sent in to gather valuable information without risking human lives.</p>
            <h2>About the Team</h2>
            <p>The GeorgeBot team is comprised of four computer engineers,
            focusing on the areas outlined below.
            <br><br><b>Jack</b> - Project leader, LiDAR, ROS, robot design and construction,
            sensors and motors
            <br><b>George</b> - LiDAR, 3D SLAM algorithm
            <br><b>Christian</b> - AWS Elastic Beanstalk configuration, web server
            <br><b>Mitchell</b> - Robot drive train, motor controller, chassis
            </p>
        </div>
      </div>
      <div class="row no-mp">
        <div class="col no-mp">
            <figure class="pic">
                <img src="../assets/preset_data.gif" alt="robot"/>
                <figcaption> INSERT ROBOT PIC HERE </figcaption>
            </figure>
        </div>
        <div class="col no-mp">
            <figure class="pic">
                <img src="../assets/preset_data.gif" alt="team"/>
                <figcaption> INSERT TEAM PIC HERE </figcaption>
            </figure>
        </div>
      </div>
    </div>

  </template>

<script>

export default {
  name: 'AboutView',
  components: {
  },
};
</script>

<style>
h2 {
    text-align: center;
    padding-top: 2vh;
}
p {
    text-align: center;
    padding-left: 5vw;
    padding-right: 5vw;
    padding-top: 2vh;
}

.pic {
    padding-top: 4vh;
    margin: auto;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 65%;
}
</style>

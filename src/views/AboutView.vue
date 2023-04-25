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
            GeorgeBot can be sent in to gather valuable information without risking human lives.
            Check out out the <a href="https://github.com/Ubspy/GeorgeBot">GeorgeBot</a> and <a href="https://github.com/cheddy1/GeorgeBotCloud">GeorgeBotCloud</a> source code!</p>
            <h2>About the Team</h2>
            <p>The GeorgeBot team is comprised of four computer engineers,
            focusing on the areas outlined below.
            <br><br><b>Jack</b> - Project leader, LiDAR, ROS, robot design and construction,
            sensors and motors
            <br><b>George</b> - LiDAR, 3D SLAM algorithm
            <br><b>Christian</b> - AWS Elastic Beanstalk configuration, web server
            backend and frontend
            <br><b>Mitchell</b> - Robot drive train, motor controller, chassis
            </p>
        </div>
      </div>
      <div class="row no-mp">
        <div class="col no-mp">
            <figure class="pic">
                <img class="bot" src="../assets/GeorgeBot.png" alt="robot"/>
                <figcaption> GeorgeBot </figcaption>
            </figure>
        </div>
        <div class="col no-mp">
            <figure class="pic">
                <img class="team" src="../assets/team.png" alt="team"/>
                <figcaption> Team GeorgeBot </figcaption>
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
    color: whitesmoke;

}
p {
    text-align: center;
    padding-left: 5vw;
    padding-right: 5vw;
    padding-top: 2vh;
    color: whitesmoke;
}

.pic {
    padding-top: 1vh;
    margin: auto;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: 65%;
    color: whitesmoke;
}

a {
  color: #9ec0e1;
}

.bot {
  width: 66%;
  height: 30vh;
}

.team {
  width: 80%;
  height: 30vh
}

</style>

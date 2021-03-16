
$(document).ready(function(){
  refreshStatCounts();
  // document.getElementById("refreshstats").addEventListener("click", test);
});

//   setInterval(refreshStatCounts, 500, )

var get_stats_endpoint = "https://2kgkqn4ohc.execute-api.ap-southeast-2.amazonaws.com/dev/stats"

// function refreshstats() {
//   console.log("Refresh Stats...")
// }

function setStats(statName, statValue) {
  // Get div containing stat count and set the new statValue
  document.getElementsByClassName(statName)[0].innerHTML = statValue;
}

async function refreshStatCounts() {
  // Get the stat counts
  const response = await fetch(get_stats_endpoint);
  const stats = await response.json();
  // Iterate over all three featured stats and update the values
  var i;
  for (i = 0; i < stats.length; i++){
    // console.log(stats[i])
    var tracked_stats = ["deaths", "accidents", "injuries"];
    var stat = stats[i]
    if (tracked_stats.includes(stat["statName"])){
      console.log(stat)
      setStats(stat["statName"], stat["statValue"])
    }
  }
}

function recordStat() {
  console.log("Refreshed...")
}
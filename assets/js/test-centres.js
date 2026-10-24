// CITB test centre town/city network — approximate coordinates for proximity search.
// Exact venue address, dates and availability are confirmed by our team when you book.
var CITB_CENTRES = [
  // London
  {name:"Central London", region:"London", postcode:"WC2", lat:51.5136, lng:-0.1210},
  {name:"Croydon", region:"London", postcode:"CR0", lat:51.3762, lng:-0.0982},
  {name:"Romford", region:"London", postcode:"RM1", lat:51.5779, lng:0.1808},
  {name:"Ilford", region:"London", postcode:"IG1", lat:51.5590, lng:0.0741},
  {name:"Enfield", region:"London", postcode:"EN1", lat:51.6521, lng:-0.0813},
  {name:"Kingston upon Thames", region:"London", postcode:"KT1", lat:51.4085, lng:-0.3064},
  {name:"Uxbridge", region:"London", postcode:"UB8", lat:51.5464, lng:-0.4787},
  // South East
  {name:"Reading", region:"South East", postcode:"RG1", lat:51.4543, lng:-0.9781},
  {name:"Oxford", region:"South East", postcode:"OX1", lat:51.7520, lng:-1.2577},
  {name:"Southampton", region:"South East", postcode:"SO14", lat:50.9097, lng:-1.4044},
  {name:"Portsmouth", region:"South East", postcode:"PO1", lat:50.8198, lng:-1.0880},
  {name:"Brighton", region:"South East", postcode:"BN1", lat:50.8225, lng:-0.1372},
  {name:"Crawley", region:"South East", postcode:"RH10", lat:51.1092, lng:-0.1872},
  {name:"Guildford", region:"South East", postcode:"GU1", lat:51.2362, lng:-0.5704},
  {name:"Maidstone", region:"South East", postcode:"ME14", lat:51.2704, lng:0.5227},
  {name:"Milton Keynes", region:"South East", postcode:"MK9", lat:52.0406, lng:-0.7594},
  {name:"Slough", region:"South East", postcode:"SL1", lat:51.5105, lng:-0.5950},
  {name:"Basingstoke", region:"South East", postcode:"RG21", lat:51.2666, lng:-1.0876},
  {name:"Medway (Chatham)", region:"South East", postcode:"ME4", lat:51.3742, lng:0.5217},
  {name:"Ashford", region:"South East", postcode:"TN23", lat:51.1465, lng:0.8724},
  {name:"Eastbourne", region:"South East", postcode:"BN21", lat:50.7687, lng:0.2713},
  {name:"Worthing", region:"South East", postcode:"BN11", lat:50.8188, lng:-0.3717},
  {name:"Woking", region:"South East", postcode:"GU21", lat:51.3168, lng:-0.5600},
  {name:"Watford", region:"South East", postcode:"WD17", lat:51.6565, lng:-0.3903},
  {name:"High Wycombe", region:"South East", postcode:"HP11", lat:51.6287, lng:-0.7482},
  {name:"Aylesbury", region:"South East", postcode:"HP20", lat:51.8156, lng:-0.8084},
  {name:"Canterbury", region:"South East", postcode:"CT1", lat:51.2802, lng:1.0789},
  {name:"Dover", region:"South East", postcode:"CT16", lat:51.1279, lng:1.3134},
  {name:"Chichester", region:"South East", postcode:"PO19", lat:50.8365, lng:-0.7792},
  {name:"Horsham", region:"South East", postcode:"RH12", lat:51.0631, lng:-0.3272},
  // South West
  {name:"Bristol", region:"South West", postcode:"BS1", lat:51.4545, lng:-2.5879},
  {name:"Plymouth", region:"South West", postcode:"PL1", lat:50.3755, lng:-4.1427},
  {name:"Exeter", region:"South West", postcode:"EX1", lat:50.7184, lng:-3.5339},
  {name:"Gloucester", region:"South West", postcode:"GL1", lat:51.8642, lng:-2.2380},
  {name:"Swindon", region:"South West", postcode:"SN1", lat:51.5558, lng:-1.7797},
  {name:"Bournemouth", region:"South West", postcode:"BH1", lat:50.7192, lng:-1.8808},
  {name:"Bath", region:"South West", postcode:"BA1", lat:51.3811, lng:-2.3590},
  {name:"Taunton", region:"South West", postcode:"TA1", lat:51.0170, lng:-3.1067},
  {name:"Truro", region:"South West", postcode:"TR1", lat:50.2632, lng:-5.0510},
  {name:"Weston-super-Mare", region:"South West", postcode:"BS23", lat:51.3459, lng:-2.9774},
  {name:"Cheltenham", region:"South West", postcode:"GL50", lat:51.9002, lng:-2.0783},
  {name:"Salisbury", region:"South West", postcode:"SP1", lat:51.0688, lng:-1.7936},
  {name:"Yeovil", region:"South West", postcode:"BA20", lat:50.9420, lng:-2.6330},
  {name:"Torquay", region:"South West", postcode:"TQ1", lat:50.4619, lng:-3.5253},
  {name:"Barnstaple", region:"South West", postcode:"EX31", lat:51.0805, lng:-4.0587},
  // East of England
  {name:"Cambridge", region:"East of England", postcode:"CB1", lat:52.2053, lng:0.1218},
  {name:"Norwich", region:"East of England", postcode:"NR1", lat:52.6309, lng:1.2974},
  {name:"Ipswich", region:"East of England", postcode:"IP1", lat:52.0567, lng:1.1482},
  {name:"Chelmsford", region:"East of England", postcode:"CM1", lat:51.7356, lng:0.4685},
  {name:"Peterborough", region:"East of England", postcode:"PE1", lat:52.5695, lng:-0.2405},
  {name:"Luton", region:"East of England", postcode:"LU1", lat:51.8787, lng:-0.4200},
  {name:"Colchester", region:"East of England", postcode:"CO1", lat:51.8959, lng:0.8919},
  {name:"Southend-on-Sea", region:"East of England", postcode:"SS1", lat:51.5459, lng:0.7077},
  {name:"Bedford", region:"East of England", postcode:"MK40", lat:52.1357, lng:-0.4666},
  {name:"St Albans", region:"East of England", postcode:"AL1", lat:51.7520, lng:-0.3360},
  {name:"Basildon", region:"East of England", postcode:"SS14", lat:51.5761, lng:0.4887},
  {name:"Stevenage", region:"East of England", postcode:"SG1", lat:51.9017, lng:-0.2019},
  // West / East Midlands
  {name:"Birmingham", region:"Midlands", postcode:"B1", lat:52.4862, lng:-1.8904},
  {name:"Coventry", region:"Midlands", postcode:"CV1", lat:52.4068, lng:-1.5197},
  {name:"Wolverhampton", region:"Midlands", postcode:"WV1", lat:52.5870, lng:-2.1288},
  {name:"Leicester", region:"Midlands", postcode:"LE1", lat:52.6369, lng:-1.1398},
  {name:"Nottingham", region:"Midlands", postcode:"NG1", lat:52.9548, lng:-1.1581},
  {name:"Derby", region:"Midlands", postcode:"DE1", lat:52.9225, lng:-1.4746},
  {name:"Northampton", region:"Midlands", postcode:"NN1", lat:52.2405, lng:-0.9027},
  {name:"Stoke-on-Trent", region:"Midlands", postcode:"ST1", lat:53.0027, lng:-2.1794},
  {name:"Worcester", region:"Midlands", postcode:"WR1", lat:52.1936, lng:-2.2215},
  {name:"Telford", region:"Midlands", postcode:"TF3", lat:52.6784, lng:-2.4453},
  {name:"Lincoln", region:"Midlands", postcode:"LN1", lat:53.2307, lng:-0.5406},
  {name:"Walsall", region:"Midlands", postcode:"WS1", lat:52.5862, lng:-1.9829},
  {name:"Dudley", region:"Midlands", postcode:"DY1", lat:52.5088, lng:-2.0899},
  {name:"Solihull", region:"Midlands", postcode:"B91", lat:52.4118, lng:-1.7776},
  {name:"Shrewsbury", region:"Midlands", postcode:"SY1", lat:52.7069, lng:-2.7538},
  {name:"Hereford", region:"Midlands", postcode:"HR1", lat:52.0567, lng:-2.7160},
  {name:"Mansfield", region:"Midlands", postcode:"NG18", lat:53.1472, lng:-1.1988},
  {name:"Chesterfield", region:"Midlands", postcode:"S40", lat:53.2350, lng:-1.4210},
  {name:"Kettering", region:"Midlands", postcode:"NN15", lat:52.3990, lng:-0.7280},
  {name:"Rugby", region:"Midlands", postcode:"CV21", lat:52.3707, lng:-1.2646},
  // Yorkshire & Humber
  {name:"Leeds", region:"Yorkshire", postcode:"LS1", lat:53.8008, lng:-1.5491},
  {name:"Sheffield", region:"Yorkshire", postcode:"S1", lat:53.3811, lng:-1.4701},
  {name:"Bradford", region:"Yorkshire", postcode:"BD1", lat:53.7960, lng:-1.7594},
  {name:"Hull", region:"Yorkshire", postcode:"HU1", lat:53.7457, lng:-0.3367},
  {name:"York", region:"Yorkshire", postcode:"YO1", lat:53.9600, lng:-1.0873},
  {name:"Wakefield", region:"Yorkshire", postcode:"WF1", lat:53.6833, lng:-1.4977},
  {name:"Doncaster", region:"Yorkshire", postcode:"DN1", lat:53.5228, lng:-1.1285},
  {name:"Huddersfield", region:"Yorkshire", postcode:"HD1", lat:53.6458, lng:-1.7850},
  {name:"Harrogate", region:"Yorkshire", postcode:"HG1", lat:53.9919, lng:-1.5378},
  {name:"Barnsley", region:"Yorkshire", postcode:"S70", lat:53.5526, lng:-1.4797},
  {name:"Rotherham", region:"Yorkshire", postcode:"S60", lat:53.4302, lng:-1.3568},
  {name:"Halifax", region:"Yorkshire", postcode:"HX1", lat:53.7218, lng:-1.8631},
  {name:"Scarborough", region:"Yorkshire", postcode:"YO11", lat:54.2830, lng:-0.4000},
  // North West
  {name:"Manchester", region:"North West", postcode:"M1", lat:53.4808, lng:-2.2426},
  {name:"Liverpool", region:"North West", postcode:"L1", lat:53.4084, lng:-2.9916},
  {name:"Preston", region:"North West", postcode:"PR1", lat:53.7632, lng:-2.7031},
  {name:"Blackpool", region:"North West", postcode:"FY1", lat:53.8175, lng:-3.0357},
  {name:"Bolton", region:"North West", postcode:"BL1", lat:53.5769, lng:-2.4282},
  {name:"Stockport", region:"North West", postcode:"SK1", lat:53.4084, lng:-2.1494},
  {name:"Warrington", region:"North West", postcode:"WA1", lat:53.3900, lng:-2.5970},
  {name:"Wigan", region:"North West", postcode:"WN1", lat:53.5450, lng:-2.6318},
  {name:"Oldham", region:"North West", postcode:"OL1", lat:53.5409, lng:-2.1114},
  {name:"Blackburn", region:"North West", postcode:"BB1", lat:53.7486, lng:-2.4823},
  {name:"Carlisle", region:"North West", postcode:"CA1", lat:54.8951, lng:-2.9382},
  {name:"Lancaster", region:"North West", postcode:"LA1", lat:54.0466, lng:-2.8007},
  {name:"Chester", region:"North West", postcode:"CH1", lat:53.1934, lng:-2.8931},
  {name:"Crewe", region:"North West", postcode:"CW1", lat:53.0977, lng:-2.4423},
  {name:"Rochdale", region:"North West", postcode:"OL16", lat:53.6097, lng:-2.1561},
  {name:"Salford", region:"North West", postcode:"M5", lat:53.4875, lng:-2.2901},
  {name:"Southport", region:"North West", postcode:"PR8", lat:53.6458, lng:-3.0067},
  {name:"St Helens", region:"North West", postcode:"WA10", lat:53.4527, lng:-2.7365},
  {name:"Barrow-in-Furness", region:"North West", postcode:"LA14", lat:54.1108, lng:-3.2280},
  // North East
  {name:"Newcastle upon Tyne", region:"North East", postcode:"NE1", lat:54.9783, lng:-1.6178},
  {name:"Sunderland", region:"North East", postcode:"SR1", lat:54.9069, lng:-1.3838},
  {name:"Middlesbrough", region:"North East", postcode:"TS1", lat:54.5742, lng:-1.2350},
  {name:"Durham", region:"North East", postcode:"DH1", lat:54.7761, lng:-1.5733},
  {name:"Darlington", region:"North East", postcode:"DL1", lat:54.5253, lng:-1.5541},
  {name:"Gateshead", region:"North East", postcode:"NE8", lat:54.9526, lng:-1.6033},
  {name:"Hartlepool", region:"North East", postcode:"TS24", lat:54.6860, lng:-1.2130},
  {name:"Stockton-on-Tees", region:"North East", postcode:"TS18", lat:54.5700, lng:-1.3170},
  // Wales
  {name:"Cardiff", region:"Wales", postcode:"CF10", lat:51.4816, lng:-3.1791},
  {name:"Swansea", region:"Wales", postcode:"SA1", lat:51.6214, lng:-3.9436},
  {name:"Newport", region:"Wales", postcode:"NP20", lat:51.5842, lng:-2.9977},
  {name:"Wrexham", region:"Wales", postcode:"LL11", lat:53.0478, lng:-2.9916},
  {name:"Bangor", region:"Wales", postcode:"LL57", lat:53.2280, lng:-4.1290},
  {name:"Aberystwyth", region:"Wales", postcode:"SY23", lat:52.4153, lng:-4.0829},
  {name:"Merthyr Tydfil", region:"Wales", postcode:"CF47", lat:51.7466, lng:-3.3781},
  // Scotland
  {name:"Glasgow", region:"Scotland", postcode:"G1", lat:55.8642, lng:-4.2518},
  {name:"Edinburgh", region:"Scotland", postcode:"EH1", lat:55.9533, lng:-3.1883},
  {name:"Aberdeen", region:"Scotland", postcode:"AB10", lat:57.1497, lng:-2.0943},
  {name:"Dundee", region:"Scotland", postcode:"DD1", lat:56.4620, lng:-2.9707},
  {name:"Inverness", region:"Scotland", postcode:"IV1", lat:57.4778, lng:-4.2247},
  {name:"Stirling", region:"Scotland", postcode:"FK8", lat:56.1165, lng:-3.9369},
  {name:"Perth", region:"Scotland", postcode:"PH1", lat:56.3950, lng:-3.4308},
  {name:"Paisley", region:"Scotland", postcode:"PA1", lat:55.8456, lng:-4.4239},
  {name:"East Kilbride", region:"Scotland", postcode:"G74", lat:55.7642, lng:-4.1770},
  {name:"Livingston", region:"Scotland", postcode:"EH54", lat:55.8850, lng:-3.5230},
  {name:"Falkirk", region:"Scotland", postcode:"FK1", lat:56.0019, lng:-3.7839},
  {name:"Ayr", region:"Scotland", postcode:"KA7", lat:55.4586, lng:-4.6292},
  {name:"Kilmarnock", region:"Scotland", postcode:"KA1", lat:55.6111, lng:-4.4956},
  {name:"Dumfries", region:"Scotland", postcode:"DG1", lat:55.0700, lng:-3.6050},
  // Northern Ireland
  {name:"Belfast", region:"Northern Ireland", postcode:"BT1", lat:54.5973, lng:-5.9301},
  {name:"Derry / Londonderry", region:"Northern Ireland", postcode:"BT48", lat:54.9966, lng:-7.3086},
  {name:"Lisburn", region:"Northern Ireland", postcode:"BT28", lat:54.5104, lng:-6.0367},
  {name:"Newry", region:"Northern Ireland", postcode:"BT35", lat:54.1751, lng:-6.3402},
  {name:"Armagh", region:"Northern Ireland", postcode:"BT61", lat:54.3503, lng:-6.6528},
  {name:"Ballymena", region:"Northern Ireland", postcode:"BT43", lat:54.8641, lng:-6.2778}
];

(function () {
  function haversineMiles(lat1, lng1, lat2, lng2) {
    var R = 3958.8; // Earth radius in miles
    var dLat = (lat2 - lat1) * Math.PI / 180;
    var dLng = (lng2 - lng1) * Math.PI / 180;
    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
      Math.sin(dLng / 2) * Math.sin(dLng / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
  }

  function nearestCentres(lat, lng, count) {
    return CITB_CENTRES
      .map(function (c) { return Object.assign({}, c, { distance: haversineMiles(lat, lng, c.lat, c.lng) }); })
      .sort(function (a, b) { return a.distance - b.distance; })
      .slice(0, count || 8);
  }

  function renderResults(list, originLabel) {
    var results = document.querySelector("#centre-results");
    var summary = document.querySelector("#centre-results-summary");
    if (!results) return;
    if (!list.length) {
      results.innerHTML = "";
      summary.textContent = "";
      return;
    }
    summary.textContent = "Nearest approved test centres to " + originLabel + ":";
    results.innerHTML = list.map(function (c, i) {
      return '<div class="centre-card">' +
        '<div class="centre-card__rank">' + (i + 1) + '</div>' +
        '<div class="centre-card__body">' +
          '<h4>' + c.name + '</h4>' +
          '<p>' + c.region + ' &middot; ' + c.postcode + ' area</p>' +
        '</div>' +
        '<div class="centre-card__distance">' + c.distance.toFixed(1) + ' mi</div>' +
        '<a href="contact.html" class="btn btn-sm btn-primary">Book Here</a>' +
      '</div>';
    }).join("");
  }

  function showError(message) {
    var summary = document.querySelector("#centre-results-summary");
    var results = document.querySelector("#centre-results");
    if (results) results.innerHTML = "";
    if (summary) summary.innerHTML = '<span style="color:#c62828;">' + message + '</span>';
  }

  function setLoading(isLoading) {
    var btn = document.querySelector("#centre-search-btn");
    if (!btn) return;
    btn.disabled = isLoading;
    btn.textContent = isLoading ? "Searching…" : "Find My Nearest Centre";
  }

  function renderRegionBrowser() {
    var container = document.querySelector("#centre-regions");
    if (!container) return;
    var byRegion = {};
    var order = [];
    CITB_CENTRES.forEach(function (c) {
      if (!byRegion[c.region]) { byRegion[c.region] = []; order.push(c.region); }
      byRegion[c.region].push(c.name);
    });
    container.innerHTML = order.map(function (region) {
      var chips = byRegion[region].sort().map(function (n) { return "<span>" + n + "</span>"; }).join("");
      return '<div class="region-group"><h4>' + region + ' (' + byRegion[region].length + ')</h4><div class="region-group__chips">' + chips + '</div></div>';
    }).join("");
  }

  document.addEventListener("DOMContentLoaded", function () {
    renderRegionBrowser();

    var form = document.querySelector("#centre-search-form");
    if (!form) return;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = document.querySelector("#centre-postcode");
      var postcode = (input.value || "").trim();
      if (!postcode) {
        showError("Please enter a postcode to search.");
        return;
      }
      setLoading(true);
      fetch("https://api.postcodes.io/postcodes/" + encodeURIComponent(postcode))
        .then(function (res) {
          if (!res.ok) throw new Error("not found");
          return res.json();
        })
        .then(function (data) {
          setLoading(false);
          var lat = data.result.latitude;
          var lng = data.result.longitude;
          var label = data.result.postcode;
          renderResults(nearestCentres(lat, lng, 8), label);
          document.querySelector("#centre-results-wrap").scrollIntoView({ behavior: "smooth", block: "start" });
        })
        .catch(function () {
          setLoading(false);
          showError("We couldn't find that postcode. Please double check it, or call us on 0203 400 8738 and we'll find your nearest centre for you.");
        });
    });

    var geoBtn = document.querySelector("#centre-geo-btn");
    if (geoBtn && "geolocation" in navigator) {
      geoBtn.addEventListener("click", function () {
        setLoading(true);
        navigator.geolocation.getCurrentPosition(
          function (pos) {
            setLoading(false);
            renderResults(nearestCentres(pos.coords.latitude, pos.coords.longitude, 8), "your current location");
            document.querySelector("#centre-results-wrap").scrollIntoView({ behavior: "smooth", block: "start" });
          },
          function () {
            setLoading(false);
            showError("We couldn't access your location. Please search by postcode instead.");
          }
        );
      });
    } else if (geoBtn) {
      geoBtn.style.display = "none";
    }
  });
})();

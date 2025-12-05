const app = Vue.createApp({
    data() {
        return {
            inputHours: 0,
            inputMinutes: 0,
            display: "",
            totalSeconds: 0,
            timerId: null,

            menuOpen: false,
            sunscreen: '',
            sunBtn: {
                src: './img/SunBtn.png',
                desc: 'Sun Button',
            },
            moonBtn: {
                src: './img/MoonBtn.png',
                desc: 'Moon Button',
            },
            lightSwitch: {
                src: './img/LightOnBtn.png',
                desc: 'Light Switch',
            },
            nightSwitch: {
                src: './img/LightOffBtn.png',
                desc: 'Night Switch',   
            },
            blindsOpen: {
                src: './img/CurtainOpen.png',
                desc: 'Blinds Open',
            },
            blindsClose: {
                src: './img/CurtainClosed.png',
                desc: 'Blinds Close',
            },
            savedEnergy: 5,

            city: 'Roskilde',
            // data: [
            //     {date: '27/11/2025', time: '13:30', lightIntensity: 0},
            //     {date: '30/11/2025', time: '14:00', lightIntensity: 120},
            // ],

            //PUT DATABASE DATA IN HERE
            date: '27/11/2025',
            time: '13:30',
            lightIntensity: 0.5,

            uvResult: [],


        }
    },
    created(){
        this.getData();
    },
    methods: {
        Show(){
            this.show = !this.show;
        },

        toggleMenu(){
            this.menuOpen = !this.menuOpen;
        },
        needSunscreen() {
            if (this.uvResult.uv >= 3) {
                this.sunscreen = 'Sunscreen needed!';
            } 
            else {
                this.sunscreen = 'No sunscreen needed';
            }
        },
        async getData() {
            try {
                // For testing only: put your real key here or (better) fetch it from your server
                const API_KEY = 'openuv-2oqfkrmipsgvri-io';

                // OpenUV expects either x-access-token or Authorization: Bearer <key>
                // Using x-access-token header:
                const headers = { 'x-access-token': API_KEY };

                // replace these with dynamic values if you want
                const lat = 55.63085267988983;   // Copenhagen latitude example
                const lng = 12.078241812295092;   // Copenhagen longitude example

                const url = `https://api.openuv.io/api/v1/uv?lat=${lat}&lng=${lng}`;

                const response = await axios.get(url, { headers });
                this.uvResult = response.data.result;
                console.log(response.data);
                this.needSunscreen();
            } catch (error) {
                console.error(error);
            }
        },
    getDataFromDatabase() {
        try {
        const url = 'https://lightmeasurement-d3hfh3aqfucmf7f4.swedencentral-01.azurewebsites.net/api/LightSensor';
        
        const response = axios.get(url);
               
                console.log(response.data);
                this.needSunscreen();
            } 
            catch (error) {
                console.error(error);
            }
    },
         timer() {
                        // Stop timer if it's running
            if (this.timerId) {
                clearInterval(this.timerId);
                this.timerId = null;
                this.timerRunning = false;
                this.display = "00:00:00";
                this.totalSeconds = 0;
                return;
            }

            // Get values from data, NOT the DOM
            let h = this.inputHours;
            let m = this.inputMinutes;

            // Convert to seconds
            this.totalSeconds = h * 3600 + m * 60;

            if (this.totalSeconds <= 0) {
                alert("Please enter a valid duration.");
                return;
            }

            // Initial display
            this.updateDisplay();
            this.timerRunning = true;

            // Start countdown
            this.timerId = setInterval(() => {
                this.totalSeconds--;

                this.updateDisplay();

                if (this.totalSeconds <= 0) {
                    clearInterval(this.timerId);
                    this.timerId = null;
                    this.timerRunning = false;
                    // INSERT LIGHT LEVEL LOGIC HERE FROM DATABASE 
                    alert("Time's up! The light level is: HIGH/LOW");
                }
            }, 1000);
        },

        updateDisplay() {
            let h = Math.floor(this.totalSeconds / 3600);
            let m = Math.floor((this.totalSeconds % 3600) / 60);
            let s = this.totalSeconds % 60;

            this.display =
                String(h).padStart(2, "0") + ":" +
                String(m).padStart(2, "0") + ":" +
                String(s).padStart(2, "0");
        }
    },
    computed: {
        myComputed() {
            return ''
        },
        
    }
})
app.mount('#app')
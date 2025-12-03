const app = Vue.createApp({
    data() {
        return {
            intro: 'Welcome to my Vue template',
            show: true,
            petname: "Pet Name",
            species: "Species",
            petlist: [
                {petname: 'Kiki', species: 'Cat'},
                {petname: 'Molly', species: 'Cat'},
                {petname: 'Rover', species: 'Dog'},
                {petname: 'Polly', species: 'Bird'},],
            image: {
                src: './img/catBanner.jpg',
                desc: 'two rows of cat drawings',
            },

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

            city: 'Copenhagen',
            // data: [
            //     {date: '27/11/2025', time: '13:30', lightIntensity: 0},
            //     {date: '30/11/2025', time: '14:00', lightIntensity: 120},
            // ],
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

    },
    computed: {
        myComputed() {
            return ''
        },
        
    }
})
app.mount('#app')
//weather java script backend
document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector('.container');
    const search = document.querySelector('.search-box button');
    const weatherBox = document.querySelector('.weather-box');
    const weatherDetails = document.querySelector('.weather-details');
    const error404 = document.querySelector('.not-found');
    const cityHide = document.querySelector('.city-hide');

    search.addEventListener('click', function () {
        const APIKey = '3927527a830a6dd02e14e9d2087c86b7';
        const cityInput = document.querySelector('.search-box input');
        const city = cityInput.value.trim();

        if (!city) return;

        fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=imperial&appid=${APIKey}`)
            .then(response => response.json())
            .then(json => {
                if (json.cod === '404') {
                    cityHide.textContent = city;
                    container.style.height = '400px';
                    weatherBox.classList.remove('active');
                    weatherDetails.classList.remove('active');
                    error404.classList.add('active');
                } else {
                    updateWeatherDetails(json);
                }
            });
    });

    function updateWeatherDetails(json) {
        const image = document.querySelector('.weather-box img');
        const temperature = document.querySelector('.weather-box .temperature');
        const description = document.querySelector('.weather-box .description');
        const humidity = document.querySelector('.weather-details .humidity span');
        const wind = document.querySelector('.weather-details .wind span');

        if (cityHide.textContent === json.name) {
            return; // No change in city, no need to update
        }

        cityHide.textContent = json.name; // Update hidden field with city name
        container.style.height = '555px';
        container.classList.add('active');
        weatherBox.classList.add('active');
        weatherDetails.classList.add('active');
        error404.classList.remove('active');

        // Dynamically update the weather image based on the 'main' field from the weather data
        image.src = baseUrl + getWeatherImageName(json.weather[0].main);

        // Update weather details
        temperature.innerHTML = `${Math.round(json.main.temp)}<span>°F</span>`;
        description.textContent = json.weather[0].description;
        humidity.textContent = `${json.main.humidity}%`;
        wind.textContent = `${Math.round(json.wind.speed)}Km/h`;

        // Temporarily remove the 'active' class to reset the animation
        container.classList.remove('active');
        weatherBox.classList.remove('active');
        weatherDetails.classList.remove('active');

        // Use a slight delay before re-adding the 'active' class to re-trigger the animation
        setTimeout(() => {
            container.classList.add('active');
            weatherBox.classList.add('active');
            weatherDetails.classList.add('active');
        }, 10); // 10 milliseconds is usually enough to reset the state

        //To stop the content from disappearing
        //setTimeout(() => {
        //container.classList.remove('active');
        //}, 2500);
    }

    function getWeatherImageName(weatherType) {
        switch (weatherType) {
            case 'Clear':
                return 'clear.png';
            case 'Rain':
                return 'rain.png';
            case 'Snow':
                return 'snow.png';
            case 'Clouds':
                return 'cloud.png';
            case 'Mist':
            case 'Haze':
                return 'mist.png';
            default:
                return 'cloud.png';
        }
    }
});
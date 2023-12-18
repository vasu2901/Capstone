var form = document.getElementById('predictform')
form.addEventListener('submit', prediction);
function prediction(event){

    /* [radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst] */
    event.preventDefault();
    const username = document.querySelector('#username').value;
    const radius_mean = document.querySelector('#radius_mean').value;
    const texture_mean = document.querySelector('#texture_mean').value;
    const perimeter_mean = document.querySelector('#perimeter_mean').value;
    const area_mean = document.querySelector('#area_mean').value;
    const smoothness_mean = document.querySelector('#smoothness_mean').value;
    const compactness_mean = document.querySelector('#compactness_mean').value;
    const concavity_mean = document.querySelector('#concavity_mean').value;
    const concave_points_mean = document.querySelector('#concave_points_mean').value;
    const symmetry_mean = document.querySelector('#symmetry_mean').value;
    const fractal_dimension_mean = document.querySelector('#fractal_dimension_mean').value;
    fetch('/predictweb', {
        method: "POST",
        body: JSON.stringify({
            username : username,
            radius: radius_mean,
            texture: texture_mean,
            perimeter: perimeter_mean,
            area: area_mean,
            smoothness: smoothness_mean,
            compactness: compactness_mean,
            concavity: concavity_mean,
            concave_points: concave_points_mean,
            symmetry: symmetry_mean,
            fractal_dimension: fractal_dimension_mean
          })
    }).then(response => response.json())
    .then(res => {
        form.style.display = 'none'
        const ele = document.getElementById('result')
        ele.style.display = 'block'
        ele.innerHTML = res.res
        const ele0 = document.getElementById('predictcontainer')
        ele0.style.marginTop = "5%"
        ele0.style.color = 'white'
    })
}

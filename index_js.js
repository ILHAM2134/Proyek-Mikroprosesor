var suhuData, kelembapanData, intensitasData, waktu;

firebase.database().ref("Monitoring").child("Kelas").on('value', (snapshot) => {
    const data = snapshot.val()
    suhuData = data.suhu
    kelembapanData = data.kelembapan
    intensitasData = data.intensitas
    waktu = data.time

    document.getElementById("p_1").innerHTML = suhuData;
    document.getElementById("p_2").innerHTML = kelembapanData;
    document.getElementById("p_3").innerHTML = intensitasData;
    
    if(parseFloat(suhuData)<29 && parseFloat(suhuData)>20){
        document.getElementById("dataSuhu").innerHTML = "Nyaman";
    }else{
        document.getElementById("dataSuhu").innerHTML = "Tidak Nyaman";
    }
    
    if(parseFloat(kelembapanData)<60 && parseFloat(kelembapanData)>40){
        document.getElementById("dataKel").innerHTML = "Nyaman";
    }else{
        document.getElementById("dataKel").innerHTML = "Tidak Nyaman";
    }
    
    if(parseFloat(intensitasData)>300){
        document.getElementById("dataIntent").innerHTML = "Nyaman";
    }else{
        document.getElementById("dataIntent").innerHTML = "Tidak Nyaman";
    }
    
    
})

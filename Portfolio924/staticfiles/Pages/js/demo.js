
    onload = function() {
        if ('speechSynthesis' in window) with(speechSynthesis) {
          console.log("YEP")
        var player = document.querySelector('#play');
        var pauser = document.querySelector('#pause');
        var stopper = document.querySelector('#stop');
        var flag = false;
      
        player.addEventListener('click', onClickPlay);
        pauser.addEventListener('click', onClickPause);
        stopper.addEventListener('click', onClickStop);
      
        function onClickPlay() {
          var icon=document.querySelector(".fas.fa-microphone-alt");
          icon.className="fas fa-microphone-alt fa-spin";
          if (!flag) {
          flag = true;
          console.log("YEP")
          utterance = new SpeechSynthesisUtterance(document.getElementsByClassName("full-article-wrapper")[0].textContent);
          
          if(getVoices()[2].name=="Microsoft Zira - English (United States)"){
                 utterance.voice = getVoices()[2];
          }
          else if (getVoices()[1].name=="Microsoft Zira - English (United States)"){
                utterance.voice = getVoices()[1];
          }
          else{
            utterance.voice = getVoices()[1];
          }
    
    
          utterance.onend = function() {
            flag = false;
            player.className = pauser.className = '';
            stopper.className = 'stopped';
          var icon=document.querySelector(".fas.fa-microphone-alt.fa-spin");
          icon.className="fas fa-microphone-alt";
          };
          player.className = 'played';
          stopper.className = '';
          utterance.rate = rate.value;
          speak(utterance);
          }
    
    
          if (paused) { /* unpause/resume narration */
          player.className = 'played';
          pauser.className = '';
          utterance.rate = rate.value;
          resume();
          }
    
    
        }
      
        function onClickPause() {
          var icon=document.querySelector(".fas.fa-microphone-alt.fa-spin");
          icon.className="fas fa-microphone-alt";
          if (speaking && !paused) { /* pause narration */
          pauser.className = 'paused';
          player.className = '';
          utterance.rate = rate.value;
          pause();
          }
        }
      
        function onClickStop() {
          var icon=document.querySelector(".fas.fa-microphone-alt.fa-spin");
          icon.className="fas fa-microphone-alt";
          if (speaking) { /* stop narration */
          /* for safari */
          stopper.className = 'stopped';
          player.className = pauser.className = '';
          utterance.rate = rate.value;
          flag = false;
          cancel();
      
          }
        }
    
      
        }
      
        else {
          alert("Speech support not found for this page or browser!")
        
        }
      
      }
      
    
      listenClicker = document.querySelector("#listen")
      listenClicker.addEventListener("click", event => {
        var listen_box = document.querySelector("#controls");
          listen_box.classList.toggle("show");
        var audio = document.querySelector("#audio");
          audio.classList.toggle("hidden");
      })
    
    
      function testing() {
          var player = document.querySelector('#play');
          var pauser = document.querySelector('#pause');
          var stopper = document.querySelector('#stop');
    
          stopper.className = 'stopped';
          player.className = pauser.className = '';
          utterance.rate = rate.value;
          flag = false;
          speechSynthesis.cancel();
      
          utterance = new SpeechSynthesisUtterance(document.getElementsByClassName("full-article-wrapper")[0].textContent);
          utterance.rate = rate.value;
    
          var icon=document.querySelector(".fas.fa-microphone-alt.fa-spin");
          icon.className="fas fa-microphone-alt";
        }
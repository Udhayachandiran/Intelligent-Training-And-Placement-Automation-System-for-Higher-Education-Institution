const rightMiniDiv = document.querySelector('.right-mini');
  const addMiniBtn = document.querySelector('.add-mini-btn');
  const deleteMiniBtn = document.querySelector('.delete-mini-btn');
  let projMinis = []; // an array to store all the proj-mini divs
  //for education section
  const rightMiniDiv2 = document.querySelector('.right-mini-2');
  const addMiniBtn2 = document.querySelector('.add-mini-btn-2');
  const deleteMiniBtn2 = document.querySelector('.delete-mini-btn-2');
  let eduMinis = []; //an array to store all the edu-mini divs

  addMiniBtn2.addEventListener('click',() => {
    //create new edu-mini div and append it to right-mini-2 div
    const newEduMini = document.createElement('div');
    newEduMini.classList.add('edu-mini');
    newEduMini.innerHTML = `
        <div class = "edu-name">
        <span class = "edu-label"> Name of Institute: </span>
        <span class="edu-text">Click the button to add a name</span>
        <button class = "edu-edit-btn">Edit</button>
        <div class = "edu-input-wrapper">
            <input type ="text" class = "edu-input-field" placeholder = "Enter Institute Name">
            <button class = "edu-save-btn">Save</button>
        </div>
        </div>
        <div class = "edu-place">
        <span class = "edu-label-2"> Place of Education: </span>
        <span class="edu-text-2">Click the button to add a name</span>
        <button class = "edu-edit-btn-2">Edit</button>
        <div class = "edu-input-wrapper-2">
            <input type ="text" class = "edu-input-field-2" placeholder = "Enter Institute Name">
            <button class = "edu-save-btn-2">Save</button>
        </div>
        </div>
        <div class = "edu-yop">
        <span class = "edu-label-3"> Year of Passing </span>
        <span class="edu-text-3">Click the button to add a name</span>
        <button class = "edu-edit-btn-3">Edit</button>
        <div class = "edu-input-wrapper-3">
            <input type ="text" class = "edu-input-field-3" placeholder = "Enter Institute Name">
            <button class = "edu-save-btn-3">Save</button>
        </div>
        </div>


    `;
    rightMiniDiv2.appendChild(newEduMini);
    eduMinis.push(newEduMini);
    //add consts for edu mini div
    const editBtnEdu = newEduMini.querySelector('.edu-edit-btn');
    const inputWrapperEdu = newEduMini.querySelector('.edu-input-wrapper');
    const inputFieldEdu = newEduMini.querySelector('.edu-input-field');
    const EduNameTextEdu = newEduMini.querySelector('.edu-name .edu-text');
    const saveBtnEdu = newEduMini.querySelector('.edu-save-btn');
    
    editBtnEdu.addEventListener('click', () => {
        EduNameTextEdu.style.display = 'none'; // hide the original text
        inputWrapperEdu.style.display = 'inline-block'; // show the input field
      });

    saveBtnEdu.addEventListener('click', () => {
        console.log("saveBtnEdu works")
      const EduName = inputFieldEdu.value;
      console.log(EduName)
      EduNameTextEdu.textContent = EduName; // set the text content of proj-name div
      inputWrapperEdu.style.display = 'none'; // hide the input field
      EduNameTextEdu.style.display = 'inline-block'; // show the new text
    });
    //set 2 for edu-place
    const editBtnEdu2 = newEduMini.querySelector('.edu-edit-btn-2');
    const inputWrapperEdu2 = newEduMini.querySelector('.edu-input-wrapper-2');
    const inputFieldEdu2 = newEduMini.querySelector('.edu-input-field-2');
    const EduNameTextEdu2 = newEduMini.querySelector('.edu-place .edu-text-2');
    const saveBtnEdu2 = newEduMini.querySelector('.edu-save-btn-2');
    editBtnEdu2.addEventListener('click', () => {
        EduNameTextEdu2.style.display = 'none'; // hide the original text
        inputWrapperEdu2.style.display = 'inline-block'; // show the input field
      });

    saveBtnEdu2.addEventListener('click', () => {
        console.log("saveBtnEdu2 works")
      const EduName2 = inputFieldEdu2.value;
      console.log(EduName2)
      EduNameTextEdu2.textContent = EduName2; // set the text content of proj-name div
      inputWrapperEdu2.style.display = 'none'; // hide the input field
      EduNameTextEdu2.style.display = 'inline-block'; // show the new text
    });
    //set 3 for edu-yop
    const editBtnEdu3 = newEduMini.querySelector('.edu-edit-btn-3');
    const inputWrapperEdu3 = newEduMini.querySelector('.edu-input-wrapper-3');
    const inputFieldEdu3 = newEduMini.querySelector('.edu-input-field-3');
    const EduNameTextEdu3 = newEduMini.querySelector('.edu-yop .edu-text-3');
    const saveBtnEdu3 = newEduMini.querySelector('.edu-save-btn-3');
    editBtnEdu3.addEventListener('click', () => {
        EduNameTextEdu3.style.display = 'none'; // hide the original text
        inputWrapperEdu3.style.display = 'inline-block'; // show the input field
      });

    saveBtnEdu3.addEventListener('click', () => {
        console.log("saveBtnEdu3 works")
      const EduName3 = inputFieldEdu3.value;
      console.log(EduName3)
      EduNameTextEdu3.textContent = EduName3; // set the text content of proj-name div
      inputWrapperEdu3.style.display = 'none'; // hide the input field
      EduNameTextEdu3.style.display = 'inline-block'; // show the new text
    });
  });


  //for project section
  addMiniBtn.addEventListener('click', () => {
    // create a new proj-mini div and append it to the right-mini div
    const newProjMini = document.createElement('div');
    newProjMini.classList.add('proj-mini');
    newProjMini.innerHTML = `
      <div class="proj-name">
        <span class="label">Project Name: </span>
        <span class="text">Click the button to add a name</span>
        <button class="edit-btn">Edit</button>
        <div class="input-wrapper">
          <input type="text" class="input-field" placeholder="Enter project name">
          <button class="save-btn">Save</button>
        </div>
      </div>
      <div class="proj-desc">
      <!-- contents of proj-desc div -->
      <span class="label-2">Project Description: </span>
      <span class="text-2">Click the button to give desc</span>
      <button class="edit-btn-2">Edit</button>
      <div class="input-wrapper-2">
        <input type="text" class="input-field-2" placeholder="Enter project name">
        <button class="save-btn-2">Save</button>
      </div>
      <!--end contents of proj-desc div-->
      </div>
      <hr>
    `;
    rightMiniDiv.appendChild(newProjMini);
    projMinis.push(newProjMini); // add the new proj-mini to the projMinis array

    // add event listeners to the new proj-mini div's edit and save buttons
    const editBtn = newProjMini.querySelector('.edit-btn');
    const inputWrapper = newProjMini.querySelector('.input-wrapper');
    const inputField = newProjMini.querySelector('.input-field');
    const projNameText = newProjMini.querySelector('.proj-name .text');
    const saveBtn = newProjMini.querySelector('.save-btn');

    editBtn.addEventListener('click', () => {
      projNameText.style.display = 'none'; // hide the original text
      inputWrapper.style.display = 'inline-block'; // show the input field
    });

    saveBtn.addEventListener('click', () => {
      const projectName = inputField.value;
      projNameText.textContent = projectName; // set the text content of proj-name div
      inputWrapper.style.display = 'none'; // hide the input field
      projNameText.style.display = 'inline-block'; // show the new text
    });
    //repeat for 2nd set
    //add event listeners for set 2
    const editBtn2 = newProjMini.querySelector('.edit-btn-2');
    const inputWrapper2 = newProjMini.querySelector('.input-wrapper-2');
    const inputField2 = newProjMini.querySelector('.input-field-2');
    const projDescText = newProjMini.querySelector('.proj-desc .text-2');
    const saveBtn2 = newProjMini.querySelector('.save-btn-2');


    editBtn2.addEventListener('click', () => {
        projDescText.style.display = 'none'; // hide the original text
        inputWrapper2.style.display = 'inline-block'; // show the input field
      });
      saveBtn2.addEventListener('click', () => {
        const projectDesc = inputField2.value;
        projDescText.textContent = projectDesc; // set the text content of proj-name div
        inputWrapper2.style.display = 'none'; // hide the input field
        projDescText.style.display = 'inline-block'; // show the new text
      });
      
  });
  deleteMiniBtn2.addEventListener('click', () => {
    if (eduMinis.length > 0) {
      const latestEduMini = eduMinis.pop(); // remove the last proj-mini from the projMinis array
      latestEduMini.remove(); // remove the latest proj-mini from the DOM
    }
  });

  deleteMiniBtn.addEventListener('click', () => {
    if (projMinis.length > 0) {
      const latestProjMini = projMinis.pop(); // remove the last proj-mini from the projMinis array
      latestProjMini.remove(); // remove the latest proj-mini from the DOM
    }
  });

  //skill section
  const addSkillBtn = document.getElementById('add-skill-btn');
const deleteSkillBtn = document.getElementById('delete-skill-btn');
const resumeSkillsDiv = document.querySelector('.resume-skills');

addSkillBtn.addEventListener('click', () => {
  const inputDiv = document.createElement('div');
  const skillInput = document.createElement('input');
  skillInput.type = 'text';
  skillInput.id = 'skill-input';
  skillInput.placeholder = 'Enter your skill';
  const submitBtn = document.createElement('button');
  submitBtn.textContent = 'Submit';
  inputDiv.appendChild(skillInput);
  inputDiv.appendChild(submitBtn);
  resumeSkillsDiv.appendChild(inputDiv);

  submitBtn.addEventListener('click', () => {
    const skillName = skillInput.value.trim();
    if (skillName !== '') {
      const skillSpan = document.createElement('span');
      skillSpan.textContent = skillName;
      skillSpan.classList.add('badge', 'bg-secondary', 'badge-lg', 'skill-tablet');
      resumeSkillsDiv.appendChild(skillSpan);
      inputDiv.remove();
    }
  });
});

deleteSkillBtn.addEventListener('click', () => {
  const latestSkillSpan = resumeSkillsDiv.lastChild;
  if (latestSkillSpan) {
    latestSkillSpan.remove();
  }
});

//interest section
const addInterestBtn = document.getElementById('add-interest-btn');
const deleteInterestBtn = document.getElementById('delete-interest-btn');
const resumeInterestDiv = document.querySelector('.resume-interest');

addInterestBtn.addEventListener('click', () => {
  const inputDiv2 = document.createElement('div');
  const interestInput = document.createElement('input');
  interestInput.type = 'text';
  interestInput.id = 'interest-input';
  interestInput.placeholder = 'Enter your skill';
  const submitBtn2 = document.createElement('button');
  submitBtn2.textContent = 'Submit';
  inputDiv2.appendChild(interestInput);
  inputDiv2.appendChild(submitBtn2);
  resumeInterestDiv.appendChild(inputDiv2);

  submitBtn2.addEventListener('click', () => {
    const interestName = interestInput.value.trim();
    if (interestName !== '') {
      const interestSpan = document.createElement('span');
      interestSpan.textContent = interestName;
      interestSpan.classList.add('badge', 'bg-secondary', 'badge-lg', 'skill-tablet');
      resumeInterestDiv.appendChild(interestSpan);
      inputDiv2.remove();
    }
  });
});

deleteSkillBtn.addEventListener('click', () => {
  const latestInterestSpan = resumeInterestDiv.lastChild;
  if (latestInterestSpan) {
    latestInterestSpan.remove();
  }
});

//for printing print-content div
function printContent() {
    console.log("print button clicked")
    var divContents = document.getElementById("print-content").innerHTML;
    var printWindow = window.open('', '', 'height=500,width=500');
    printWindow.document.write('<html><head><title>Print Contents</title>');
    printWindow.document.write('</head><body>');
    printWindow.document.write(divContents);
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.print();
  }

  function printDiv() {
    var content = document.getElementById("print-content").innerHTML;
    var mywindow = window.open('', 'Print', 'height=600,width=800');
  
    mywindow.document.write('<html><head><title>Print</title>');
    mywindow.document.write('<style></style>');
    mywindow.document.write('</head><body>');
    mywindow.document.write(content);
    mywindow.document.write('</body></html>');
  
    mywindow.document.close();
    mywindow.focus()
    mywindow.print();
    mywindow.close();
  
    return true;
  }
  //another piece of print code
  function printDiv2() {
    var printContents = document.getElementById("print-content").innerHTML;
    var originalContents = document.body.innerHTML;
  
    document.body.innerHTML = printContents;
  
    var cssUrl = '/resources/style.css';
    var head = document.head || document.getElementsByTagName('head')[0];
    var style = document.createElement('link');
    style.href = cssUrl;
    style.rel = 'stylesheet';
    style.type = 'text/css';
    head.appendChild(style);
  
    window.print();
  
    document.body.innerHTML = originalContents;
  }
  
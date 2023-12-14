document.addEventListener("DOMContentLoaded", () => {
  const allCards = document.getElementById("allCards");
  const allCardsFilter = document.getElementById("allCardsFilter");
  const filterForm = document.getElementById("filterForm");
  const filterFormMain = document.getElementById("filterForm");
  const mainForm = document.getElementById("mainForm");

  let lang = document.getElementById("lang").selectedIndex;

  let urlAllList = "http://127.0.0.1:8000/flat";
  let localUrl;
  let to_sea;

  if (localStorage.filter !== undefined) {
    localUrl = JSON.parse(localStorage.filter);
  }

  if (localStorage.to_sea !== undefined) {
    to_sea = JSON.parse(localStorage.to_sea);
  }

  function btnObj() {
    const btnVilla = document.getElementById("btnVilla");
    const btnZdanie = document.getElementById("btnZdanie");
    const btnZemlia = document.getElementById("btnZemlia");
    const btnKvartira = document.getElementById("btnKvartira");
    const btnPenthouse = document.getElementById("btnPenthouse");
    const btnKomm = document.getElementById("btnKomm");
    const btnTownhouse = document.getElementById("btnTownhouse");
    const btnOtel = document.getElementById("btnOtel");

    if (btnVilla) {
      btnVilla.addEventListener("click", () => {
        const urlVillaList =
          "http://127.0.0.1:8000/flat?title=&price=&square=&description=&main_type_real_estate=8";
        allCards.innerHTML = "";
        loadFlatList(urlVillaList);
      });
    }
    if (btnZdanie) {
      btnZdanie.addEventListener("click", () => {
        const urlZdanieList =
          "http://127.0.0.1:8000/flat?title=&price=&square=&description=&main_type_real_estate=6";
        allCards.innerHTML = "";
        loadFlatList(urlZdanieList);
      });
    }

    if (btnZemlia) {
      btnZemlia.addEventListener("click", () => {
        const urlZemliaList =
          "http://127.0.0.1:8000/flat?title=&price=&square=&description=&main_type_real_estate=3";
        allCards.innerHTML = "";
        loadFlatList(urlZemliaList);
      });
    }

    if (btnKvartira) {
      btnKvartira.addEventListener("click", () => {
        const urlKvartiraList =
          "http://127.0.0.1:8000/flat?title=&price=&square=&description=&main_type_real_estate=2";
        allCards.innerHTML = "";
        loadFlatList(urlKvartiraList);
      });
    }

    if (btnPenthouse) {
      btnPenthouse.addEventListener("click", () => {
        const urlPenthouseList =
          "http://127.0.0.1:8000/flat?title=&price=&square=&description=&main_type_real_estate=5";
        allCards.innerHTML = "";
        loadFlatList(urlPenthouseList);
      });
    }

    if (btnKomm) {
      btnKomm.addEventListener("click", () => {
        const urlKommList =
          "http://127.0.0.1:8000/flat?title=&price=&square=&description=&main_type_real_estate=1";
        allCards.innerHTML = "";
        loadFlatList(urlKommList);
      });
    }
    if (btnTownhouse) {
      btnTownhouse.addEventListener("click", () => {
        const urlTownhouseList =
          "http://127.0.0.1:8000/flat?title=&price=&square=&description=&main_type_real_estate=4";
        allCards.innerHTML = "";
        loadFlatList(urlTownhouseList);
      });
    }

    if (btnOtel) {
      btnOtel.addEventListener("click", () => {
        const urlOtelList =
          "http://127.0.0.1:8000/flat?title=&price=&square=&description=&main_type_real_estate=7";
        allCards.innerHTML = "";
        loadFlatList(urlOtelList);
      });
    }
  }

  function mainFormFunc() {
    mainForm.addEventListener("submit", () => {
      const formData = new FormData(mainForm);

      let main_city = formData.get("main_city");
      if (!main_city) {
        main_city = "";
      }

      let main_district = formData.get("main_district");
      if (!main_district) {
        main_district = "";
      }

      let main_country = formData.get("main_country");
      if (!main_country) {
        main_country = "";
      }

      let main_type_real_estate = formData.get("main_type_real_estate");
      if (!main_type_real_estate) {
        main_type_real_estate = "";
      }

      let main_status = formData.get("main_status");
      if (!main_status) {
        main_status = "";
      }

      let main_infrastructure = formData.get("main_infrastructure");
      if (!main_infrastructure) {
        main_infrastructure = "";
      }

      let sea = formData.get("to_sea");
      if (!sea) {
        sea = "";
      }

      let request = `http://127.0.0.1:8000/flat?main_country=${main_country}&main_district=${main_district}&main_city=${main_city}&main_type_real_estate=${main_type_real_estate}&main_status=${main_status}&main_infrastructure=${main_infrastructure}`;

      allCards.innerHTML = "";

      localStorage.clear();
      localStorage.filter = JSON.stringify({ filter: request });
      localStorage.to_sea = JSON.stringify({ filter_sea: sea });
    });
  }

  function filterFormFunc() {
    filterForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const formData = new FormData(filterForm);

      let main_city = formData.get("main_city");
      if (!main_city) {
        main_city = "";
      }

      let main_district = formData.get("main_district");
      if (!main_district) {
        main_district = "";
      }

      let main_country = formData.get("main_country");
      if (!main_country) {
        main_country = "";
      }

      let main_type_real_estate = formData.get("main_type_real_estate");
      if (!main_type_real_estate) {
        main_type_real_estate = "";
      }

      let main_status = formData.get("main_status");
      if (!main_status) {
        main_status = "";
      }

      let main_infrastructure = formData.get("main_infrastructure");
      if (!main_infrastructure) {
        main_infrastructure = "";
      }

      let sea = formData.get("to_sea");
      if (!sea) {
        sea = "";
      }
      console.log(sea);

      let request = `http://127.0.0.1:8000/flat?main_country=${main_country}&main_district=${main_district}&main_city=${main_city}&main_type_real_estate=${main_type_real_estate}&main_status=${main_status}&main_infrastructure=${main_infrastructure}`;

      if (allCardsFilter) allCardsFilter.innerHTML = "";

      localStorage.clear();
      localStorage.filter = JSON.stringify({ filter: request });
      localStorage.to_sea = JSON.stringify({ filter_sea: sea });

      loadFlatListFilter(request);
    });
  }

  async function loadFlatListFilter(url) {
    const response = await fetch(url);
    const data = await response.json();

    if (data["count"] === 0) {
      switch (lang) {
        case 0:
          allCardsFilter.innerHTML =
            "<h2>Currently there are no results in the selected category</h2>";
          break;
        case 1:
          allCardsFilter.innerHTML =
            "<h2>На данный момент нет результатов в выбранной категории</h2>";
          break;
        case 2:
          allCardsFilter.innerHTML =
            "<h2>Şu anda seçilen kategoride sonuç yok</h2>";
          break;
        case 3:
          allCardsFilter.innerHTML =
            "<h2>حاليا لا توجد نتائج في الفئة المحددة</h2>";
          break;
        case 4:
          allCardsFilter.innerHTML =
            "<h2>در حال حاضر هیچ نتیجه ای در دسته بندی انتخاب شده وجود ندارد</h2>";
          break;
        default:
          break;
      }
    }
    let seaNum = JSON.parse(localStorage.to_sea);

    for (let i = 0; i < data["results"].length && i < 100; i++) {
      if (
        Number(data["results"][i]["to_sea"]) <= Number(seaNum["filter_sea"]) &&
        Number(data["results"][i]["to_sea"]) !== 0
      ) {
        allCardsFilter.append(
          createCardItm(
            data["results"][i]["id"],
            data["results"][i]["main_photo"],
            data["results"][i]["title"],
            data["results"][i]["main_city"],
            data["results"][i]["main_district"],
            data["results"][i]["main_rooms"],
            data["results"][i]["square"],
            data["results"][i]["price"],
            data["results"][i]["main_type_real_estate"],
            allCardsFilter
          )
        );
      }
      if (Number(seaNum["filter_sea"]) === 0) {
        allCardsFilter.append(
          createCardItm(
            data["results"][i]["id"],
            data["results"][i]["main_photo"],
            data["results"][i]["title"],
            data["results"][i]["main_city"],
            data["results"][i]["main_district"],
            data["results"][i]["main_rooms"],
            data["results"][i]["square"],
            data["results"][i]["price"],
            data["results"][i]["main_type_real_estate"],
            allCardsFilter
          )
        );
      }
    }
    if (allCardsFilter.textContent === "") {
      allCardsFilter.innerHTML =
        "<h2>На данный момент нет результатов в выбранной категории</h2>";
    }
  }

  function filterFormMainFunc() {
    filterFormMain.addEventListener("submit", (e) => {
      const formData = new FormData(filterForm);

      let main_city = formData.get("main_city");
      if (!main_city) {
        main_city = "";
      }

      let main_district = formData.get("main_district");
      if (!main_district) {
        main_district = "";
      }

      let main_country = formData.get("main_country");
      if (!main_country) {
        main_country = "";
      }

      let main_type_real_estate = formData.get("main_type_real_estate");
      if (!main_type_real_estate) {
        main_type_real_estate = "";
      }

      to_sea = formData.get("to_sea");
      if (!to_sea) {
        to_sea = "";
      }
      let request = `http://127.0.0.1:8000/flat?main_country=${main_country}&main_district=${main_district}&main_city=${main_city}&main_type_real_estate=${main_type_real_estate}`;
      if (allCards) allCards.innerHTML = "";
    });
  }

  async function loadFlatList(url) {
    const response = await fetch(url);
    const data = await response.json();

    if (data["count"] === 0) {
      allCards.innerHTML =
        "<h2>На данный момент нет результатов в выбранной категории</h2>";
    }

    for (let i = 0; i < data["results"].length && i < 8; i++) {
      if (data["results"][i]) {
        allCards.append(
          createCardItm(
            data["results"][i]["id"],
            data["results"][i]["main_photo"],
            data["results"][i]["title"],
            data["results"][i]["main_city"],
            data["results"][i]["main_district"],
            data["results"][i]["main_rooms"],
            data["results"][i]["square"],
            data["results"][i]["price"],
            data["results"][i]["main_type_real_estate"]
          )
        );
      } else {
        return;
      }
    }
  }

  function createCardItm(
    id,
    main_photo,
    title,
    main_city,
    main_district,
    rooms,
    square,
    price,
    main_type_real_estate,
    cardId = allCards
  ) {
    const allCardsLi = document.createElement("li");
    allCardsLi.classList.add("newobj-cards__card");

    const allCardsLink = document.createElement("a");
    allCardsLink.href = `http://127.0.0.1:8000/${id}`;

    const divNewobj = document.createElement("div");
    divNewobj.classList.add("newobj-cards__card-top");

    const imgSlide1 = document.createElement("img");
    imgSlide1.src = `${main_photo}`;
    imgSlide1.alt = `${title}`;
    const spanTitle = document.createElement("span");
    spanTitle.textContent = `${title}`;

    allCardsLi.append(allCardsLink);
    allCardsLink.append(divNewobj);
    divNewobj.append(spanTitle);
    divNewobj.append(imgSlide1);

    const divNewobjBottom = document.createElement("div");
    divNewobjBottom.classList.add("newobj-cards__card-bottom");

    const propertyUl = document.createElement("ul");
    propertyUl.classList.add("propety-card");

    const propertyLi1 = document.createElement("li");
    propertyLi1.classList.add("property-card__itm", "card-geo");

    const divCardLink = document.createElement("div");
    divCardLink.classList.add("card-link");
    const divCardLink1 = document.createElement("a");
    divCardLink1.href = `${main_city}`;
    divCardLink1.textContent = `${main_city}`;
    const divCardLink2 = document.createElement("a");
    divCardLink2.classList.add("card-link__two");
    divCardLink2.href = `${main_district}`;
    if (main_district) divCardLink2.textContent = ` / ${main_district}`;
    divCardLink.append(divCardLink1, divCardLink2);
    propertyLi1.append(divCardLink);

    const propertyLi2 = document.createElement("li");
    propertyLi2.classList.add("property-card__itm", "card-rooms");
    const divCardLink3 = document.createElement("a");
    divCardLink3.href = `${rooms}`;
    if (rooms) {
      divCardLink3.textContent = `${rooms}`;
    } else {
      divCardLink3.textContent = `${main_type_real_estate}`;
    }
    propertyLi2.append(divCardLink3);

    const propertyLi3 = document.createElement("li");
    propertyLi3.classList.add("property-card__itm", "card-square");
    const divCardLink4 = document.createElement("a");
    if (square) {
      divCardLink4.href = `${square}`;
      divCardLink4.textContent = `${square} m2`;
    } else {
      divCardLink4.textContent = "Подробности по телефону";
    }
    propertyLi3.append(divCardLink4);

    const propertyLi4 = document.createElement("li");
    propertyLi4.classList.add("property-card__itm", "card-price");
    const divCardLink5 = document.createElement("span");
    price = String(price);
    switch (price.length) {
      case 4:
        divCardLink5.textContent = `${price[0]} ${price[1]}${price[2]}${price[3]}`;
        break;
      case 5:
        divCardLink5.textContent = `${price[0]}${price[1]} ${price[2]}${price[3]}${price[4]}`;
        break;
      case 6:
        divCardLink5.textContent = `${price[0]}${price[1]}${price[2]} ${price[3]}${price[4]}${price[5]}`;
        break;
      case 7:
        divCardLink5.textContent = `${price[0]} ${price[1]}${price[2]}${price[3]} ${price[4]}${price[5]}${price[6]}`;
        break;
      case 8:
        divCardLink5.textContent = `${price[0]}${price[1]} ${price[2]}${price[3]}${price[4]} ${price[5]}${price[6]}${price[7]}`;
        break;
      case 9:
        divCardLink5.textContent = `${price[0]}${price[1]}${price[2]} ${price[3]}${price[4]}${price[5]} ${price[6]}${price[7]}${price[8]}`;
        break;

      default:
        divCardLink5.textContent = `${price[0]}`;
        break;
    }
    propertyLi4.append(divCardLink5);

    allCardsLi.append(divNewobjBottom);
    divNewobjBottom.append(propertyUl);
    propertyUl.append(propertyLi1);
    propertyUl.append(propertyLi2);
    propertyUl.append(propertyLi3);
    propertyUl.append(propertyLi4);

    cardId.append(allCardsLi);
    return allCardsLi;
  }

  function cardPrice() {
    const cardPrice = document.querySelectorAll(".card-price");

    for (let i = 0; i < cardPrice.length; i++) {
      const element = cardPrice[i].textContent.trim();

      cardPrice[i].innerHTML = "<span>dsfdsf</span>";

      switch (element.length) {
        case 4:
          cardPrice[
            i
          ].innerHTML = `<span>${element[0]} ${element[1]}${element[2]}${element[3]}</span>`;
          break;
        case 5:
          cardPrice[
            i
          ].innerHTML = `<span>${element[0]}${element[1]} ${element[2]}${element[3]}${element[4]}</span>`;
          break;
        case 6:
          cardPrice[
            i
          ].innerHTML = `<span>${element[0]}${element[1]}${element[2]} ${element[3]}${element[4]}${element[5]}</span>`;
          break;
        case 7:
          cardPrice[
            i
          ].innerHTML = `<span>${element[0]} ${element[1]}${element[2]}${element[3]} ${element[4]}${element[5]}${element[6]}</span>`;
          break;
        case 8:
          cardPrice[
            i
          ].innerHTML = `<span>${element[0]}${element[1]} ${element[2]}${element[3]}${element[4]} ${element[5]}${element[6]}${element[7]}</span>`;
          break;
        case 9:
          cardPrice[
            i
          ].innerHTML = `<span>${element[0]}${element[1]}${element[2]} ${element[3]}${element[4]}${element[5]} ${element[6]}${element[7]}${element[8]}</span>`;
          break;

        default:
          cardPrice[i].innerHTML = `<span>${element[0]}</span>`;
          break;
      }
    }
  }

  const modalOpen = document.getElementById("modalOpen");
  const modalBlock = document.getElementById("modalBlock");

  function modal() {
    modalOpen.addEventListener("click", (e) => {
      modalBlock.classList.remove("hidden");
    });
  }

  const modalCloseBtn = document.getElementById("modalCloseBtn");
  function modelClose() {
    modalCloseBtn.addEventListener("click", () => {
      modalBlock.classList.add("hidden");
    });
    const overlay = document.getElementById("overlay");
    overlay.addEventListener("click", () => {
      modalBlock.classList.add("hidden");
    });
  }

  const modalQuest = document.getElementById("modalQuest");
  modalQuest.addEventListener("click", () => {
    modalBlock.classList.remove("hidden");
  });

  const mobMenuBtn = document.getElementById("mobMenuBtn");
  const mobMenu = document.getElementById("mobMenu");

  mobMenuBtn.addEventListener("click", () => {
    mobMenu.classList.toggle("hidden");
    if (mobMenu.classList.contains("hidden")) {
      switch (lang) {
        case 0:
          mobMenuBtn.textContent = "Open menu";
          break;
        case 1:
          mobMenuBtn.textContent = "Открыть меню";
          break;
        case 2:
          mobMenuBtn.textContent = "Menüyü aç";
          break;
        case 3:
          mobMenuBtn.textContent = "افتح القائمة";
          break;
        case 4:
          mobMenuBtn.textContent = "منو را باز کنید";
          break;

        default:
          break;
      }
    } else {
      switch (lang) {
        case 0:
          mobMenuBtn.textContent = "Close menu";
          break;
        case 1:
          mobMenuBtn.textContent = "Закрыть меню";
          break;
        case 2:
          mobMenuBtn.textContent = "Menüyü kapat";
          break;
        case 3:
          mobMenuBtn.textContent = "أغلق القائمة";
          break;
        case 4:
          mobMenuBtn.textContent = "منو را ببندید";
          break;

        default:
          break;
      }
    }
  });

  switch (lang) {
    case 0:
      mobMenuBtn.textContent = "Open menu";
      break;
    case 1:
      mobMenuBtn.textContent = "Открыть меню";
      break;
    case 2:
      mobMenuBtn.textContent = "Menüyü aç";
      break;
    case 3:
      mobMenuBtn.textContent = "افتح القائمة";
      break;
    case 4:
      mobMenuBtn.textContent = "منو را باز کنید";
      break;

    default:
      break;
  }

  setTimeout(() => {
    // const jivo = document.querySelector('.__jivoMobileButton')
    // console.log(jivo.childNodes)
    // jivo.classList.add('jivoTop')
    // const jivo = document.querySelector()
  }, 1000)

  btnObj();
  cardPrice();
  if (modalOpen) modal();
  if (modalCloseBtn) modelClose();

  if (mainForm) mainFormFunc();

  if (allCards) loadFlatList(urlAllList);
  if (allCardsFilter) loadFlatListFilter(localUrl.filter);

  if (filterForm) filterFormFunc();
  if (filterFormMain) filterFormMainFunc();
});

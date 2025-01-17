window.addEventListener("load", () => {
  const mobileMenuBtn = document.querySelector("[data-mobileMenuBtn]");
  const menuContainer = document.querySelector("[data-menuContainer]");

  mobileMenuBtn.addEventListener("click", () => {
    if (!menuContainer.hasAttribute("data-mobileMenuActive")) {
      menuContainer.setAttribute("data-mobileMenuActive", "");
      mobileMenuBtn.innerHTML = `
        <svg viewBox="0 0 511.991 511.991" width="24" height="24">
          <g class="fill-white">
          	<path d="M286.161,255.867L505.745,36.283c8.185-8.474,7.951-21.98-0.523-30.165c-8.267-7.985-21.375-7.985-29.642,0   L255.995,225.702L36.411,6.118c-8.475-8.185-21.98-7.95-30.165,0.524c-7.985,8.267-7.985,21.374,0,29.641L225.83,255.867   L6.246,475.451c-8.328,8.331-8.328,21.835,0,30.165l0,0c8.331,8.328,21.835,8.328,30.165,0l219.584-219.584l219.584,219.584   c8.331,8.328,21.835,8.328,30.165,0l0,0c8.328-8.331,8.328-21.835,0-30.165L286.161,255.867z"/>
          </g>
        </svg>
      `;
      menuContainer.classList.add(
        "max-[768px]:left-[0px]",
        "max-[768px]:transition-all",
        "max-[768px]:duration-300",
      );
    } else {
      menuContainer.removeAttribute("data-mobileMenuActive");
      mobileMenuBtn.innerHTML = `
        <svg viewBox="0 0 490.667 490.667" width="24" height="24">
          <g class="fill-white">
            <path
              d="M469.333,224h-448C9.551,224,0,233.551,0,245.333c0,11.782,9.551,21.333,21.333,21.333h448   c11.782,0,21.333-9.551,21.333-21.333C490.667,233.551,481.115,224,469.333,224z" />
            <path
              d="M21.333,117.333h448c11.782,0,21.333-9.551,21.333-21.333s-9.551-21.333-21.333-21.333h-448C9.551,74.667,0,84.218,0,96   S9.551,117.333,21.333,117.333z" />
            <path
              d="M469.333,373.333h-448C9.551,373.333,0,382.885,0,394.667C0,406.449,9.551,416,21.333,416h448   c11.782,0,21.333-9.551,21.333-21.333C490.667,382.885,481.115,373.333,469.333,373.333z" />
          </g>
        </svg>
      `;
      menuContainer.classList.remove("max-[768px]:left-[0px]");
      menuContainer.classList.add("max-[768px]:left-[-5000px]");
    }
  });
});
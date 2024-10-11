<template>
  <footer class="bg-[#404040] text-white relative min-h-[398px]">
    <img class="absolute top-0 left-0" src="../assets/images/triangle-black-4.png" alt="" />
    <p class="text-[64px] leading-[52px] text-center pt-[80px] mb-[86px] footer-title">Связаться</p>
    <div class="flex mx-auto justify-between items-center max-w-[616px] gap-[80px] mb-[71px] contacts__inner">
      <div class="flex justify-between items-center gap-[14px] contacts__box">
        <div class="">
          <img src="../assets/images/mail-icon.svg" alt="Значок конвертика" />
        </div>
        <div class="flex justify-between flex-col">
          <span class="text-[18px] contacts__box-title">Email</span>
          <span class="font-medium contacts__box-text">glebmorozov@gmail.com</span>
          <span class="font-medium contacts__box-text">glebmorozov@gmail.com</span>
        </div>
      </div>
      <div class="flex justify-between items-center gap-[14px]">
        <div class="">
          <img src="../assets/images/phone-icon.svg" alt="Значок телефона" />
        </div>
        <div class="flex justify-between flex-col">
          <span class="text-[18px] contacts__box-title">Телефон</span>
          <span class="font-medium contacts__box-text">+7 995 906 34 94</span>
          <span class="font-medium contacts__box-text">+7 995 906 34 94</span>
        </div>
      </div>
    </div>
    <div class="flex justify-center">
      <div class="w-[680px] border-bottom border-[1px] bg-white line"></div>
    </div>

    <div class="text-center mt-[6px] text-[13px] font-extralight pb-[46px] text-underline">
      <span>авторское право 2024</span>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style>
@media (max-width: 1024px) {
  footer {
    min-height: 300px;
  }

  .footer-title {
    font-size: 44px;
    padding-top: 50px;
    margin-bottom: 50px;
  }

  .contacts__inner {
    max-width: 480px;
    gap: 40px;
    margin-bottom: 40px;
  }

  .contacts__box {
    gap: 15px;
  }

  .contacts__box-title {
    font-size: 14px;
  }

  .contacts__box-text {
    font-size: 12px;
  }

  .line {
    width: 80%;
  }

  .text-underline {
    font-size: 10px;
    padding-bottom: 25px;
  }
}

@media (max-width: 768px) {
  footer {
    min-height: 240px;
  }

  .footer-title {
    font-size: 34px;
    padding-top: 50px;
    margin-bottom: 30px;
  }

  .contacts__inner {
    flex-direction: column;
    align-items: center;
    max-width: 90%;
    gap: 25px;
    margin-bottom: 25px;
  }

  .contacts__box {
    width: 100%;
    justify-content: center;
  }

  .contacts__box-title {
    font-size: 13px;
  }

  .contacts__box-text {
    font-size: 12px;
  }

  .line {
    width: 90%;
  }

  .text-underline {
    font-size: 11px;
    padding-bottom: 15px;
  }
}

@media (max-width: 360px) {
  footer {
    min-height: 220px;
  }

  .footer-title {
    font-size: 26px;
    padding-top: 80px;
    margin-bottom: 15px;
  }

  .contacts__inner {
    gap: 15px;
  }

  .contacts__box-title {
    font-size: 11px;
  }

  .contacts__box-text {
    font-size: 10px;
  }

  .line {
    width: 100%;
  }

  .text-underline {
    font-size: 9px;
    padding-bottom: 10px;
  }
}
</style>
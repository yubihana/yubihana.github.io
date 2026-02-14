(() => {
  const ORDER_URL = "https://yubihana.square.site/";
  const INSTAGRAM = "yubi.hana1";
  const TIKTOK = "yubi_hana8";
  const XIAOHONGSHU = "XIAOHONGSHU";
  const X = "iyubihana";

  function toSocialUrl(platform, value){
    const v = String(value || "").trim();
    if (!v || v === platform.toUpperCase()) return "";
    if (v.includes("://")) return v;
    const handle = v.replace(/^@/, "");
    if (!handle) return "";
    if (platform === "instagram") return `https://www.instagram.com/${INSTAGRAM}/`;
    if (platform === "tiktok") return `https://www.tiktok.com/@${TIKTOK}`;
    if (platform === "x") return `https://x.com/${X}`;
    return v;
  }

  for (const a of document.querySelectorAll('a[href="ORDER_URL"]')) a.href = ORDER_URL;

  const map = {
    "INSTAGRAM": toSocialUrl("instagram", INSTAGRAM),
    "TIKTOK": toSocialUrl("tiktok", TIKTOK),
    "XIAOHONGSHU": toSocialUrl("xiaohongshu", XIAOHONGSHU),
    "X": toSocialUrl("x", X),
  };

  for (const [k,v] of Object.entries(map)) {
    for (const a of document.querySelectorAll(`a[href="${k}"]`)) {
      if (!v) {
        a.removeAttribute("href");
        a.style.display = "none";
      } else {
        a.href = v;
      }
    }
  }
})();

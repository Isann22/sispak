document.addEventListener('DOMContentLoaded', () => {
  // 1. Inisialisasi Tooltips Bootstrap
  const tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]'),
  )
  tooltipTriggerList.map(
    (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl),
  )

  // 2. Logic Pencarian Gejala (Filter)
  const searchInput = document.getElementById('symptom-search')
  const symptomItems = document.querySelectorAll('.symptom-item')

  if (searchInput) {
    searchInput.addEventListener('keyup', (e) => {
      const term = e.target.value.toLowerCase()

      symptomItems.forEach((item) => {
        const text = item.innerText.toLowerCase()
        if (text.includes(term)) {
          item.style.display = '' // Tampilkan
        } else {
          item.style.display = 'none' // Sembunyikan
        }
      })
    })
  }

  // 4. Auto Scroll ke Hasil (Jika ada hasil)
  const hasilSection = document.getElementById('hasil-section')
  if (hasilSection) {
    setTimeout(() => {
      hasilSection.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }, 500) // Delay sedikit agar animasi render selesai
  }

  // 5. Animasi Loading saat Submit
  const form = document.getElementById('diagnosisForm')
  if (form) {
    form.addEventListener('submit', function () {
      const btn = this.querySelector('button[type="submit"]')
      if (btn) {
        const originalText = btn.innerHTML
        btn.disabled = true
        btn.innerHTML =
          '<span class="spinner-border spinner-border-sm me-2"></span>Menganalisa...'

        // Restore jika user menekan back (opsional, browser modern menghandle bfcache)
        setTimeout(() => {
          btn.disabled = false
          btn.innerHTML = originalText
        }, 5000)
      }
    })
  }
})

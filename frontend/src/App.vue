<script setup lang="ts">
import { ref } from 'vue'

const dashboards = [
  { id: 1, title: 'Visão Geral do Dataset' },
  { id: 2, title: 'Distribuição por Classificação' },
  { id: 3, title: 'Top 10 Municípios (Notificações)' },
  { id: 4, title: 'Distribuição por Sexo' },
  { id: 5, title: 'Casos por Faixa Etária' },
  { id: 6, title: 'Taxa de Letalidade' },
  { id: 7, title: 'Sintomas mais Frequentes' },
  { id: 8, title: 'Comorbidades nos Óbitos' },
  { id: 9, title: 'Evolução Temporal' },
  { id: 10, title: 'Letalidade por Município (Top 5)' }
]

const currentDash = ref<number | null>(null)
const isDropdownOpen = ref(false)

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8501'

const selectDash = (id: number) => {
  currentDash.value = id
  isDropdownOpen.value = false
}
</script>

<template>
  <main class="min-h-screen bg-[#0f0f16] text-[#cdd6f4] font-sans overflow-x-hidden relative">
    <nav v-if="currentDash" class="w-full flex items-center justify-between px-8 py-4 bg-[#181825] border-b border-[#313244] shadow-lg sticky top-0 z-50">
      <button @click="currentDash = null" class="flex items-center gap-2 group transition-all duration-300">
        <div class="h-10 w-10 flex items-center justify-center rounded-full bg-[#313244] group-hover:bg-[#cba6f7] transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 group-hover:text-[#11111b] transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
        </div>
        <span class="font-semibold tracking-wide text-[#b4befe] group-hover:text-[#cba6f7] transition-colors">Home</span>
      </button>

      <div class="relative">
        <button @click="isDropdownOpen = !isDropdownOpen" class="flex items-center gap-3 px-5 py-2.5 rounded-xl bg-[#313244] hover:bg-[#45475a] border border-[#585b70]/30 transition-all font-medium">
          {{ currentDash ? dashboards.find(d => d.id === currentDash)?.title : 'Selecione um Dashboard' }}
          <svg xmlns="http://www.w3.org/2000/svg" :class="isDropdownOpen ? 'rotate-180' : ''" class="w-4 h-4 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        <div v-show="isDropdownOpen" class="absolute right-0 top-14 w-72 bg-[#1e1e2e] rounded-xl border border-[#313244] shadow-2xl overflow-hidden animate-fade-in-down origin-top-right">
          <ul class="max-h-[60vh] overflow-y-auto w-full">
            <li v-for="dash in dashboards" :key="dash.id">
              <button @click="selectDash(dash.id)" :class="{'bg-[#cba6f7]/20 text-[#cba6f7] font-semibold': currentDash === dash.id, 'hover:bg-[#313244]': currentDash !== dash.id}" class="w-full text-left px-5 py-3 transition-colors border-b border-[#313244]/50 last:border-0 truncate">
                {{ dash.id }}. {{ dash.title }}
              </button>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div v-if="!currentDash" class="flex flex-col items-center justify-center min-h-[100dvh] w-full px-4 bg-gradient-to-br from-[#0f0f16] via-[#181825] to-[#0f0f16] relative pb-20">
      
      <div class="absolute inset-0 overflow-hidden pointer-events-none">
        <div class="absolute w-[500px] h-[500px] bg-[#cba6f7]/10 rounded-full blur-3xl -top-32 -left-32 animate-pulse"></div>
        <div class="absolute w-[600px] h-[600px] bg-[#89b4fa]/10 rounded-full blur-3xl bottom-0 -right-32 animate-pulse" style="animation-duration: 5s"></div>
        <div class="absolute w-[800px] h-[400px] bg-[#f9e2af]/5 rounded-full blur-3xl top-1/2 left-1/4 animate-pulse" style="animation-duration: 7s"></div>
      </div>

      <div class="max-w-4xl text-center z-10 space-y-12">
        <div class="space-y-6 animate-fade-in-up">
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#f38ba8]/10 text-[#f38ba8] border border-[#f38ba8]/20 font-semibold text-sm uppercase tracking-widest backdrop-blur-md">
            <span class="w-2 h-2 rounded-full bg-[#f38ba8] animate-ping"></span>
            Dados e Impacto
          </div>
          <h1 class="text-6xl font-extrabold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-[#cba6f7] to-[#89b4fa] leading-tight pb-2">
            O Impacto da Pandemia
          </h1>
          <p class="text-xl text-[#a6adc8] leading-relaxed max-w-2xl mx-auto font-light">
            A pandemia do COVID-19 redefiniu drasticamente a sociedade, o sistema de saúde e as relações humanas. Os dados deixam de ser apenas números quando representam as vidas diretamente afetadas, ressaltando a urgência de respostas orientadas por análises concretas.
          </p>
        </div>

        <div class="relative max-w-sm mx-auto animate-fade-in-up" style="animation-delay: 200ms">
          <button @click="isDropdownOpen = !isDropdownOpen" class="w-full flex items-center justify-between px-6 py-4 rounded-2xl bg-gradient-to-r from-[#cba6f7] to-[#89b4fa] text-[#11111b] font-bold text-lg shadow-[0_0_30px_rgba(203,166,247,0.3)] hover:shadow-[0_0_40px_rgba(203,166,247,0.5)] hover:-translate-y-1 transition-all duration-300">
            Explorar Painéis 
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          
          <div v-show="isDropdownOpen" class="absolute top-16 left-0 w-full bg-[#181825]/90 backdrop-blur-xl rounded-2xl border border-[#313244] shadow-2xl overflow-y-auto z-50">
            <ul class="max-h-[50vh] w-full">
              <li v-for="dash in dashboards" :key="dash.id">
                <button @click="selectDash(dash.id)" class="w-full text-left px-5 py-3 hover:bg-[#313244]/80 transition-colors border-b border-[#313244]/30 last:border-0 text-[#cdd6f4]">
                  {{ dash.id }}. {{ dash.title }}
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="w-full h-[calc(100vh-73px)] p-6 bg-[#0f0f16]">
      <div class="w-full h-full rounded-2xl overflow-hidden border border-[#313244] shadow-2xl bg-[#1e1e2e] relative">
        <div class="absolute inset-0 flex items-center justify-center">
            <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[#cba6f7]"></div>
        </div>
        <iframe 
          :src="`${BASE_URL}/?view=${currentDash}&embed=true&t=${Date.now()}`" 
          class="w-full h-full border-none relative z-10 bg-transparent"
          title="COVID Dashboard"
        ></iframe>
      </div>
    </div>
  </main>
</template>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

@keyframes fill-down {
  0% { transform: scaleY(0); opacity: 0; }
  100% { transform: scaleY(1); opacity: 1; }
}

.animate-fade-in-down {
  animation: fill-down 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes fade-in-up {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}

.animate-fade-in-up {
  animation: fade-in-up 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
::-webkit-scrollbar-track {
  background: #11111b;
}
::-webkit-scrollbar-thumb {
  background: #313244;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: #45475a;
}
</style>

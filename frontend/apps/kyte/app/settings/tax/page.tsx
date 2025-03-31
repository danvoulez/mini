'use client'
import useSWR from 'swr'
import axios from 'axios'

export default function TaxSettings() {
  const { data, mutate } = useSWR('/api/settings/tax', url => axios.get(url).then(res => res.data))

  const updateTax = async () => {
    await axios.put('/api/settings/tax', { tax_percentage: 8.5 })
    mutate()
  }

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">Configuração de Impostos</h1>
      <p>Imposto atual: {data?.tax_percentage}%</p>
      <button onClick={updateTax} className="bg-black text-white px-4 py-2 mt-4 rounded">
        Atualizar para 8.5%
      </button>
    </main>
  )
}
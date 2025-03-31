'use client'
import useSWR from 'swr'
import axios from 'axios'

export default function LowStock() {
  const { data } = useSWR('/api/products/low-stock', url => axios.get(url).then(res => res.data))

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">Produtos com Estoque Baixo</h1>
      <ul className="list-disc pl-5">
        {data?.map((p: any) => <li key={p.id}>{p.name} (Estoque: {p.stock})</li>)}
      </ul>
    </main>
  )
}
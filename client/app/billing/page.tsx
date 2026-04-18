const invoices = [
  { id: 'INV-1048', date: '2026-04-01', amount: '$29.00', status: 'Paid' },
  { id: 'INV-1009', date: '2026-03-01', amount: '$29.00', status: 'Paid' },
  { id: 'INV-0976', date: '2026-02-01', amount: '$29.00', status: 'Paid' },
];

export default function BillingPage() {
  return (
    <div className="space-y-6">
      <section className="card space-y-4">
        <h1 className="text-2xl font-black text-white">Billing & subscription</h1>
        <div className="grid gap-4 md:grid-cols-3">
          <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">
            <p className="text-sm text-zinc-400">Current plan</p>
            <p className="mt-2 text-xl font-bold">Pro · $29/mo</p>
          </div>
          <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">
            <p className="text-sm text-zinc-400">Next billing date</p>
            <p className="mt-2 text-xl font-bold">May 1, 2026</p>
          </div>
          <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">
            <p className="text-sm text-zinc-400">Payment method</p>
            <p className="mt-2 text-xl font-bold">Visa •••• 4242</p>
          </div>
        </div>
      </section>

      <section className="card">
        <h2 className="text-xl font-bold text-white">Invoices</h2>
        <div className="mt-4 overflow-x-auto">
          <table className="min-w-full text-left text-sm">
            <thead>
              <tr className="border-b border-zinc-800 text-zinc-400">
                <th className="py-2 pr-3">Invoice</th>
                <th className="py-2 pr-3">Date</th>
                <th className="py-2 pr-3">Amount</th>
                <th className="py-2">Status</th>
              </tr>
            </thead>
            <tbody>
              {invoices.map((invoice) => (
                <tr key={invoice.id} className="border-b border-zinc-900">
                  <td className="py-2 pr-3 font-medium text-zinc-100">{invoice.id}</td>
                  <td className="py-2 pr-3 text-zinc-300">{invoice.date}</td>
                  <td className="py-2 pr-3 text-zinc-300">{invoice.amount}</td>
                  <td className="py-2 text-emerald-300">{invoice.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}

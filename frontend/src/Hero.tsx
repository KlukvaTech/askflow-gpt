import { useMediaQuery } from './hooks';
import DocsGPT3 from './assets/klukva.svg';

export default function Hero({ className = '' }: { className?: string }) {
  // const isMobile = window.innerWidth <= 768;
  const { isMobile } = useMediaQuery();
  return (
    <div className={`mt-14 ${isMobile ? 'mb-2' : 'mb-12'}flex flex-col `}>
      <div className=" mb-2 flex items-center justify-center sm:mb-10">
        <p className="mr-2 text-4xl font-semibold">Askfow</p>
        <img className="mb-2 h-14" src={DocsGPT3} alt="Askfow" />
      </div>
      {isMobile ? (
        <p className="mb-3 text-center leading-6 text-black-1000">
          Welcome to <span className="font-bold ">Askfow</span>, your technical
          documentation assistant! Start by entering your query in the input
          field below, and we&apos;ll provide you with the most relevant
          answers.
        </p>
      ) : (
        <>
          <p className="mb-3 text-center leading-6 text-black-1000">
            Welcome to Askfow, your technical documentation assistant!
          </p>
          <p className="mb-3 text-center leading-6 text-black-1000">
            Enter a query related to the information in the documentation you
            selected to receive
            <br /> and we will provide you with the most relevant answers.
          </p>
          <p className="mb-3 text-center leading-6 text-black-1000">
            Start by entering your query in the input field below and we will do
            the rest!
          </p>
        </>
      )}
      <div
        className={`sections ${
          isMobile ? '' : 'mt-1'
        } flex flex-wrap items-center justify-center gap-2 sm:gap-1 md:gap-0`}
      >
      </div>
    </div>
  );
}

import React, { useEffect, useState, useRef } from 'react';
import BeatLoader from "react-spinners/BeatLoader";

const App = () => {
    const [messages, setMessages] = useState([]);
    const [lastMsg, setLastMsg] = useState('');
    const messagesEndRef = useRef(null);
    const [input, setInput] = useState('');
    const checkPreferences = async () => {
        try {
            const response = await fetch('/home');  // Ensure URL is correct
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);  // Check if the response is OK
            }
            const data = await response.json();
            setMessages([{ usermsg: '', MEmsg: data }]);
        } catch (error) {
            console.error('Error checking preferences:', error);
        }
    };
    useEffect(() => {
        checkPreferences();
        scrollToBottom();
    }, []);

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const message = JSON.stringify({ prompt: input });
            setLastMsg(input);
            setInput('');
            const response = await fetch('/Search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: message
            });
            const data = await response.json();
            setMessages([...messages, { usermsg: input, MEmsg: data }]);
            setLastMsg('');
        } catch (error) {
            console.error('Error fetching result:', error);
        }
    };

    return (
        <div className="guidini">
            <div className="px-[10%] p-4 border-gray-200 fixed top-0 left-0 right-0 bg-gradient-to-r from-gray-900 to-gray-700 z-10 flex flex-row items-center justify-between">
                <div className='text-white text-xl font-bold'>Morocco Explorer</div>
            </div>
            <div className="flex flex-col flex-1 relative">
                <div className="overflow-y-auto space-y-4 flex-1 mb-20">
                    <div className="messages mt-28">
                        {messages.map((message, index) => (
                            <div key={index}>
                                <div className="text-right px-[10%] flex flex-col items-end">
                                    <div className='flex items-center flex-row-reverse mb-2 '>
                                        <div>
                                            <img className='w-10 rounded-full ml-2' src={localStorage.getItem("photo")} alt='profileImg'/>
                                        </div>
                                        <div className='text-sm text-white font-bold'>
                                            {localStorage.getItem("user")}
                                        </div>
                                    </div>
                                    <div className="inline-block text-white  bg-white/5 rounded-xl px-4 py-2">
                                        {message.usermsg}
                                    </div>
                                </div>

                                <div className="text-left my-4 px-[10%] flex flex-col items-start">
                                    <div className='flex items-center flex-row mb-2 '>
                                        <div>
                                            <img className='w-10 rounded-full' src='https://cdn.countryflags.com/thumbs/morocco/flag-400.png' alt='profileImg'/>
                                        </div>
                                        <div className='text-sm text-white font-bold ml-2'>
                                            Morocco Explorer
                                        </div>
                                    </div>
                                    <div className="inline-block text-white bg-white/10 rounded-xl px-4 py-2">
                                        {message.MEmsg}
                                    </div>
                                </div>
                            </div>
                        ))}
                        {lastMsg && 
                        <div className="text-right px-[10%] flex flex-col items-end">
                            <div className='flex items-center flex-row-reverse mb-2 '>
                                <div>
                                    <img className='w-10 rounded-full ml-2' src={localStorage.getItem("photo")} alt='profileImg'/>
                                </div>
                                <div className='text-sm text-white font-bold'>
                                    {localStorage.getItem("user")}
                                </div>
                            </div>
                            <div className="inline-block text-white  bg-white/5 rounded-xl px-4 py-2"> 
                                {lastMsg} 
                            </div>
                        </div>}
                        <div ref={messagesEndRef}></div>
                    </div>
                </div>

                <div className="p-4 border-gray-200 fixed bottom-0 left-0 right-0 bg-gradient-to-r from-gray-900 to-gray-700">
                    {!lastMsg && 
                        <div className="flex gap-4  px-[10%]">
                            <form onSubmit={handleSubmit} id="fr" className="w-full relative">
                                <input
                                    type="text"
                                    name="chat"
                                    id="chat"
                                    className="flex-1 p-2 outline-none border border-gray-500 focus:border-gray-400 text-white rounded-xl w-full bg-transparent"
                                    placeholder="Enter prompt"
                                    value={input}
                                    onChange={(e) => setInput(e.target.value)}
                                />
                                <div className='flex items-center absolute bottom-1.5 right-2'>
                                    {input && 
                                        <button className=" text-white/70 hover:text-white/100 rounded font-bold mx-1" type="submit" form="fr">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                                                <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                                            </svg>
                                        </button>
                                    }
                                    {!input && 
                                        <button disabled className=" text-white/20 rounded font-bold mx-1" type="submit" form="fr">
                                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                                                <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
                                            </svg>
                                        </button>
                                    }
                                </div>
                            </form>
                        </div>
                    }
                    {lastMsg &&
                        <div className='flex justify-center'>
                            <BeatLoader 
                                color='white'
                                loading={true}
                                size={20}
                                aria-label="Loading Spinner"
                                data-testid="loader"
                            />
                        </div>
                    }
                </div>
            </div>
        </div>
    );
};

export default App;

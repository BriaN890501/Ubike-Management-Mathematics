#if defined(UNICODE) && !defined(_UNICODE)
    #define _UNICODE
#elif defined(_UNICODE) && !defined(UNICODE)
    #define UNICODE
#endif

#include <iostream>
#include <tchar.h>
#include <windows.h>
#include <windowsx.h>
#include <windef.h>
#include <wingdi.h>

using namespace std;
HWND hButton1;
HWND hButton2;
HINSTANCE appInstance;
/*  Declare Windows procedure  */
LRESULT CALLBACK WindowProcedure (HWND, UINT, WPARAM, LPARAM);

/*  Make the class name into a global variable  */
TCHAR szClassName[ ] = _T("CodeBlocksWindowsApp");

int WINAPI WinMain (HINSTANCE hThisInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR lpszArgument,
                     int nCmdShow)
{
    HWND hwnd;               /* This is the handle for our window */
    MSG messages;            /* Here messages to the application are saved */
    WNDCLASSEX wincl;        /* Data structure for the windowclass */

    /* The Window structure */
    wincl.hInstance = hThisInstance;
    wincl.lpszClassName = szClassName;
    wincl.lpfnWndProc = WindowProcedure;      /* This function is called by windows */
    wincl.style = CS_DBLCLKS;                 /* Catch double-clicks */
    wincl.cbSize = sizeof (WNDCLASSEX);

    /* Use default icon and mouse-pointer */
    wincl.hIcon = LoadIcon (NULL, IDI_APPLICATION);
    wincl.hIconSm = LoadIcon (NULL, IDI_APPLICATION);
    wincl.hCursor = LoadCursor (NULL, IDC_ARROW);
    wincl.lpszMenuName = NULL;                 /* No menu */
    wincl.cbClsExtra = 0;                      /* No extra bytes after the window class */
    wincl.cbWndExtra = 0;                      /* structure or the window instance */
    /* Use Windows's default colour as the background of the window */
    wincl.hbrBackground = (HBRUSH) COLOR_BACKGROUND;

    /* Register the window class, and if it fails quit the program */
    if (!RegisterClassEx (&wincl))
        return 0;

    /* The class is registered, let's create the program*/
    hwnd = CreateWindowEx (
           0,                   /* Extended possibilites for variation */
           szClassName,         /* Classname */
           _T("Code::Blocks Template Windows App"),       /* Title Text */
           WS_OVERLAPPEDWINDOW, /* default window */
           CW_USEDEFAULT,       /* Windows decides the position */
           CW_USEDEFAULT,       /* where the window ends up on the screen */
           2000,                 /* The programs width */
           1000,                 /* and height in pixels */
           HWND_DESKTOP,        /* The window is a child-window to desktop */
           NULL,                /* No menu */
           hThisInstance,       /* Program Instance handler */
           NULL                 /* No Window Creation data */
           );


    /* Make the window visible on the screen */
    ShowWindow (hwnd, nCmdShow);

    /* Run the message loop. It will run until GetMessage() returns 0 */
    while (GetMessage (&messages, NULL, 0, 0))
    {
        /* Translate virtual-key messages into character messages */
        TranslateMessage(&messages);
        /* Send message to WindowProcedure */
        DispatchMessage(&messages);
    }

    /* The program return-value is 0 - The value that PostQuitMessage() gave */
    return messages.wParam;
}


/*  This function is called by the Windows function DispatchMessage()  */

LRESULT CALLBACK WindowProcedure (HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    HMENU a = CreatePopupMenu();
    HBITMAP hBitmap;
    static BITMAP s_bm;
    static HDC s_hdcMem;
    //AppendMenu(a, MF_GRAYED,)

    switch (message)                  /* handle the messages */
    {
        case WM_DESTROY:
            PostQuitMessage (0);       /* send a WM_QUIT to the message queue */
            break;
        case WM_LBUTTONDOWN:
            //SetLayeredWindowAttributes(hButton1, RGB(0, 0, 0), 155, LWA_ALPHA);
            break;
        case WM_KEYDOWN:
            hButton1 = (HWND)CreateWindow(TEXT("button"),  //Button是预定义 窗体类
			                         TEXT("click"),
									 WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
									 350, 45, 160, 65,
									 hwnd,
									 (HMENU)520,  //(重点)这里设置按钮id,但是 原本是设置菜单的 所以需要HMENU
									 appInstance,
									 NULL);
            break;
        case WM_RBUTTONDOWN:
            {
            int xPos = GET_X_LPARAM(lParam);
            int yPos = GET_Y_LPARAM(lParam);
            cout << xPos << " " << yPos <<endl;
            MessageBox(hwnd,"FUCK","yeah",MB_OK);
            break;
            }
        case WM_CREATE:
        hBitmap = (HBITMAP)LoadImage(NULL, "IMG_1494040461615.jpg", IMAGE_BITMAP, 0, 0, LR_LOADFROMFILE | LR_CREATEDIBSECTION);

        if (hBitmap == NULL)
        {
            MessageBox(hwnd, "LoadImage failed", "Error", MB_ICONERROR);
            exit(0);
        }
        else
        {
            // 将背影图片放入HDC - s_hdcMem
            HDC        hdc;
            hdc = GetDC(hwnd);
            s_hdcMem = CreateCompatibleDC(hdc);
            SelectObject(s_hdcMem, hBitmap);
            ReleaseDC(hwnd, hdc);

            // 得到位图信息
            GetObject(hBitmap, sizeof(s_bm), &s_bm);
        }

        hButton1 = (HWND)CreateWindow(TEXT("button"),  //Button是预定义 窗体类
			                         TEXT("click"),
									 WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
									 350, 45, 160, 65,
									 hwnd,
									 (HMENU)520,  //(重点)这里设置按钮id,但是 原本是设置菜单的 所以需要HMENU
									 appInstance,
									 NULL);
        hButton2 = (HWND)CreateWindow(TEXT("button"),  //Button是预定义 窗体类
			                         TEXT("click2"),
									 WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
									 550, 245, 360, 265,
									 hwnd,
									 (HMENU)620,  //(重点)这里设置按钮id,但是 原本是设置菜单的 所以需要HMENU
									 appInstance,
									 NULL);
			break;
        case WM_COMMAND:
            if (LOWORD(wParam) == 520 && HIWORD(wParam) == BN_CLICKED)
            {
                MessageBox(hwnd, TEXT("yeah"), TEXT("1"), MB_OK);
            }
            if (LOWORD(wParam) == 620 && HIWORD(wParam) == BN_CLICKED)
            {
                MessageBox(hwnd, TEXT("yeah"), TEXT("2"), MB_OK);
            }
                break;
        default:                      /* for messages that we don't deal with */
            return DefWindowProc (hwnd, message, wParam, lParam);
    }

    return 0;
}
